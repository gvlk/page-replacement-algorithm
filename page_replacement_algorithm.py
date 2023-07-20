from os.path import exists


class PageReplacement:
    ALGORITHMS = {
        0: "Aging",
        1: "WSClock"
    }

    def __init__(
            self,
            algorithm: int,
            memory_lenght: int,
            input_file: str,
            page_lenght: int = 4000,
            counter_lenght: int = 8
    ) -> None:

        if algorithm in self.ALGORITHMS:
            self.algo_type = algorithm
        else:
            raise ValueError(
                f"Invalid algorithm option. Please choose from: {self.ALGORITHMS}."
            )

        if exists(input_file):
            self.input_file = input_file
        else:
            raise FileNotFoundError(
                f"The input file '{input_file}' does not exist."
            )

        self.memory_lenght = memory_lenght
        self.page_lenght = page_lenght
        self.total_pages = memory_lenght // page_lenght
        # Nesse exemplo as palavras que ocupam a memória física são representados por dois caracteres: o primeiro
        # representa a existência de um dado ou instrução naquele espaço e o segundo representa o bit de
        # referenciamento.
        self.physical_memory = ["00"] * self.total_pages
        # Memória virtual terá o dobro do tamanho da física. Uma tabela para páginas de dados e uma para páginas de
        # instruções. Primeiros caracteres representam o índice do quadro da memória física e o último caractere
        # funciona como o último bit da palavra da tabela, pois representará a existência ou não da página na memória
        # física. Portando a tabela será do tipo: página:"índice do quadro + presente em memória física"
        self.page_table = {
            "data": {key: "00" for key in range(self.total_pages)},
            "inst": {key: "00" for key in range(self.total_pages)}
        }
        self.counter_lenght = counter_lenght

    def run(self) -> str:
        result = ""
        if self.algo_type == 0:
            result = self.run_aging()
        elif self.algo_type == 1:
            result = self.run_wsclock()
        return result

    def run_aging(self) -> str:
        counters = ["0" * self.counter_lenght] * self.total_pages
        total_page_faults = 0

        script = self.read_memory_accesses()
        for access in script:
            access_info = access.split(" ")
            access_type = access_info[1]
            page_index = int(access_info[2])
            memory_frame = self.page_in_physical_memory(access_type, page_index)
            if memory_frame is None:
                # Interrupção.
                total_page_faults += 1

                # Atualiza os contadores.
                for frame_index, frame_word in enumerate(self.physical_memory):
                    counters[frame_index] = frame_word[-1] + counters[frame_index][:self.counter_lenght - 1]
                    referenced = frame_word[-1] == "1"
                    if referenced:
                        self.physical_memory[frame_index] = frame_word[:1] + "0"

                # Escolhe um quadro pouco usado para liberar.
                memory_frame = self.get_less_used_page(counters)

                # Gravar o conteúdo deste quadro no disco.
                # Simulando a gravação do conteúdo para o disco.
                self.store(memory_frame)

                # Carrega do disco a página para o quadro liberado.
                # Simulando uma requisição à memória virtual.
                self.physical_memory[memory_frame] = self.access_virtual_memory(page_index)

                # Atualiza o mapa.
                self.update_page_table(access_type, page_index, memory_frame)

            # Indica que a página foi referenciada atualizando seu bit R.
            self.physical_memory[memory_frame] = self.physical_memory[memory_frame][:1] + "1"

            # Simulando um acesso à memória física.
            self.access_memory(memory_frame)

        return f"Com o algoritmo {self.ALGORITHMS[self.algo_type]} ocorrem {total_page_faults} faltas de página."

    def run_wsclock(self) -> str:
        return f"{self.ALGORITHMS[self.algo_type]} não foi implementado ainda."

    def read_memory_accesses(self) -> str:
        with open(self.input_file, 'r') as file:
            for access in file:
                access = access.strip()
                if not access:
                    continue
                yield access

    def page_in_physical_memory(self, access_type: str, page_index: int) -> int | None:
        """
        Retorna o índice do quadro memória física ou None caso a página não esteja presente.
        """
        if access_type == "DADOS":
            table = self.page_table["data"]
        elif access_type == "INST":
            table = self.page_table["inst"]
        else:
            raise ValueError(f"Invalid access_type '{access_type}' in the script.")

        try:
            # Último bit de cada palavra na tabela representa a existência da página na memória física
            word = table[page_index]
            if word[-1] == "0":
                # Falta de página.
                return None
            else:
                # Página presente na memória física.
                return int(word[:-1])
        except KeyError:
            raise KeyError(
                f"The page with index {page_index} is not present in the page table. You need a bigger virtual memory"
            )

    def get_less_used_page(self, counters) -> int:
        less_used = -1
        min_counter = int("1" * self.counter_lenght, 2)
        for page_index, counter in enumerate(counters):
            counter_int = int(counter, 2)
            if counter_int < min_counter:
                less_used = page_index
                min_counter = counter_int
        return less_used

    def update_page_table(self, access_type: str, page_index: int, memory_frame: int) -> None:
        """
        Atualiza a tabela de páginas com o novo quadro da memória física.
        """
        if access_type == "DADOS":
            table = self.page_table["data"]
        elif access_type == "INST":
            table = self.page_table["inst"]
        else:
            raise ValueError(f"Invalid access_type '{access_type}' in the script.")

        table[page_index] = f"{memory_frame}1"

    def access_memory(self, memory_frame) -> None:
        return

    def access_virtual_memory(self, memory_address) -> str:
        return "10"

    def store(self, memory_frame) -> None:
        return
