"""Exercício 037 — Conversor de bases numéricas.

Lê um número inteiro e o converte para a base escolhida pelo usuário:
binário (base 2), octal (base 8) ou hexadecimal (base 16).

Curso em Vídeo — Python, Mundo 2 (Gustavo Guanabara).
"""

from enum import Enum
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk


# ---------------------------------------------------------------------------
# Regras de negócio (independentes da interface gráfica)
# ---------------------------------------------------------------------------

class SistemaNumerico(Enum):
    """Sistemas numéricos de destino suportados pelo conversor."""

    BINARIO = ("Binário", 2, "b")
    OCTAL = ("Octal", 8, "o")
    HEXADECIMAL = ("Hexadecimal", 16, "X")

    def __init__(self, rotulo: str, base: int, formato: str) -> None:
        self.rotulo = rotulo
        self.base = base
        self.formato = formato


def converter_numero(numero: int, sistema: SistemaNumerico) -> str:
    """Converte um número inteiro para a representação no sistema informado.

    Números negativos mantêm o sinal e o hexadecimal usa letras maiúsculas.

    >>> converter_numero(255, SistemaNumerico.BINARIO)
    '11111111'
    >>> converter_numero(255, SistemaNumerico.OCTAL)
    '377'
    >>> converter_numero(-255, SistemaNumerico.HEXADECIMAL)
    '-FF'
    >>> converter_numero(0, SistemaNumerico.BINARIO)
    '0'
    """
    return format(numero, sistema.formato)


# ---------------------------------------------------------------------------
# Identidade visual
# ---------------------------------------------------------------------------

class Cores:
    """Paleta do tema escuro usado na interface."""

    FUNDO = "#1e1e1e"
    SUPERFICIE = "#2a2a2a"
    SUPERFICIE_REALCE = "#353535"
    BORDA = "#3c3c3c"
    TEXTO = "#e0e0e0"
    TEXTO_SECUNDARIO = "#9e9e9e"
    TEXTO_DESATIVADO = "#5f5f5f"
    CIANO = "#00bcd4"
    CIANO_CLARO = "#26c6da"
    CIANO_ESCURO = "#0097a7"
    AZUL = "#4f8cff"
    VERDE = "#4caf50"
    VERMELHO = "#f44336"
    VERMELHO_ESCURO = "#d32f2f"
    BRANCO = "#ffffff"


# Fontes monoespaçadas preferidas, em ordem (Windows, macOS, Linux).
FONTES_MONOESPACADAS = ("Consolas", "Menlo", "DejaVu Sans Mono")

LARGURA_MINIMA = 380  # px
DURACAO_AVISO_COPIA = 1500  # ms


# ---------------------------------------------------------------------------
# Interface gráfica
# ---------------------------------------------------------------------------

class ConversorApp(tk.Tk):
    """Janela principal do conversor de bases numéricas."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Conversor de Bases Numéricas — Exercício 37")
        self.configure(background=Cores.FUNDO)
        self.resizable(False, False)

        # Último número convertido com sucesso (None = nada a exibir).
        self._numero: int | None = None
        self._aviso_copia_id: str | None = None

        self._texto_numero = tk.StringVar()
        self._sistema = tk.StringVar(value=SistemaNumerico.BINARIO.name)
        self._legenda = tk.StringVar()
        self._resultado = tk.StringVar()
        self._erro = tk.StringVar()

        self._criar_fontes()
        self._configurar_estilos()
        self._montar_interface()
        self._registrar_eventos()

        self._exibir_resultado()
        self._centralizar_janela()
        self._campo_numero.focus_set()

    # -- Configuração -------------------------------------------------------

    def _criar_fontes(self) -> None:
        """Cria as fontes a partir da fonte padrão do sistema operacional."""
        padrao = tkfont.nametofont("TkDefaultFont").actual()
        familia_ui = padrao["family"]
        tamanho = abs(padrao["size"])

        disponiveis = set(tkfont.families(self))
        familia_mono = next(
            (familia for familia in FONTES_MONOESPACADAS if familia in disponiveis),
            tkfont.nametofont("TkFixedFont").actual("family"),
        )

        self._fonte_texto = tkfont.Font(self, family=familia_ui, size=tamanho)
        self._fonte_destaque = tkfont.Font(self, family=familia_ui, size=tamanho, weight="bold")
        self._fonte_legenda = tkfont.Font(self, family=familia_ui, size=tamanho - 1, weight="bold")
        self._fonte_titulo = tkfont.Font(self, family=familia_ui, size=tamanho + 5, weight="bold")
        self._fonte_numero = tkfont.Font(self, family=familia_mono, size=tamanho + 4)
        self._fonte_resultado = tkfont.Font(self, family=familia_mono, size=tamanho + 8, weight="bold")

    def _configurar_estilos(self) -> None:
        """Define os estilos ttk do tema escuro.

        O tema "clam" é usado porque, ao contrário dos temas nativos
        (como o Aqua do macOS), respeita cores personalizadas em botões e
        campos, garantindo a mesma aparência em todos os sistemas.
        """
        estilo = ttk.Style(self)
        estilo.theme_use("clam")

        estilo.configure(
            ".",
            background=Cores.FUNDO,
            foreground=Cores.TEXTO,
            font=self._fonte_texto,
            selectbackground=Cores.CIANO,
            selectforeground=Cores.FUNDO,
        )
        estilo.map(
            ".",
            background=[("disabled", Cores.FUNDO), ("active", Cores.FUNDO)],
            foreground=[("disabled", Cores.TEXTO_DESATIVADO)],
            selectbackground=[("!focus", Cores.BORDA)],
            selectforeground=[("!focus", Cores.TEXTO)],
        )

        # Textos
        estilo.configure("Titulo.TLabel", foreground=Cores.AZUL, font=self._fonte_titulo)
        estilo.configure("Subtitulo.TLabel", foreground=Cores.VERDE)
        estilo.configure("Legenda.TLabel", foreground=Cores.TEXTO_SECUNDARIO, font=self._fonte_legenda)
        estilo.configure("Erro.TLabel", foreground=Cores.VERMELHO)
        estilo.configure("Discreto.TLabel", foreground=Cores.TEXTO_SECUNDARIO)

        # Campo de entrada: borda ciano com foco e vermelha quando inválido
        estilo.configure(
            "TEntry",
            fieldbackground=Cores.SUPERFICIE,
            foreground=Cores.TEXTO,
            insertcolor=Cores.TEXTO,
            bordercolor=Cores.BORDA,
            lightcolor=Cores.SUPERFICIE,
            padding=(10, 8),
        )
        estilo.map(
            "TEntry",
            bordercolor=[("invalid", Cores.VERMELHO), ("focus", Cores.CIANO)],
            lightcolor=[("invalid", Cores.VERMELHO), ("focus", Cores.CIANO)],
        )

        # Resultado: campo somente leitura com aparência de texto (permite seleção)
        estilo.configure(
            "Resultado.TEntry",
            fieldbackground=Cores.FUNDO,
            foreground=Cores.VERDE,
            bordercolor=Cores.FUNDO,
            lightcolor=Cores.FUNDO,
            padding=0,
        )
        estilo.map(
            "Resultado.TEntry",
            fieldbackground=[("readonly", Cores.FUNDO)],
            bordercolor=[("focus", Cores.FUNDO)],
            lightcolor=[("focus", Cores.FUNDO)],
        )

        # Seletor de sistema numérico (botões segmentados)
        estilo.configure(
            "Segmento.Toolbutton",
            background=Cores.SUPERFICIE,
            foreground=Cores.TEXTO,
            bordercolor=Cores.BORDA,
            focuscolor=Cores.TEXTO_SECUNDARIO,
            relief="solid",
            anchor="center",
            padding=(8, 8),
        )
        estilo.map(
            "Segmento.Toolbutton",
            relief=[("", "solid")],
            background=[
                ("selected", Cores.CIANO),
                ("pressed", Cores.BORDA),
                ("active", Cores.SUPERFICIE_REALCE),
            ],
            foreground=[("selected", Cores.FUNDO)],
            bordercolor=[("selected", Cores.CIANO)],
            focuscolor=[("selected", Cores.FUNDO)],
            font=[("selected", self._fonte_destaque)],
        )

        self._configurar_botao(
            "Primario.TButton",
            fundo=(Cores.CIANO, Cores.CIANO_CLARO, Cores.CIANO_ESCURO),
            texto=(Cores.FUNDO, Cores.FUNDO),
            borda=Cores.CIANO,
            font=self._fonte_destaque,
            padding=(16, 10),
        )
        self._configurar_botao(
            "Secundario.TButton",
            fundo=(Cores.SUPERFICIE, Cores.SUPERFICIE_REALCE, Cores.BORDA),
            texto=(Cores.TEXTO, Cores.TEXTO),
            borda=Cores.BORDA,
            padding=(10, 6),
        )
        self._configurar_botao(
            "Perigo.TButton",
            fundo=(Cores.FUNDO, Cores.VERMELHO, Cores.VERMELHO_ESCURO),
            texto=(Cores.VERMELHO, Cores.BRANCO),
            borda=Cores.VERMELHO,
            padding=(14, 6),
        )

    def _configurar_botao(
        self,
        nome: str,
        fundo: tuple[str, str, str],
        texto: tuple[str, str],
        borda: str,
        **opcoes: object,
    ) -> None:
        """Cria um estilo de botão com estados normal, hover e pressionado.

        Args:
            nome: nome do estilo ttk (ex.: "Primario.TButton").
            fundo: cores de fundo (normal, hover, pressionado).
            texto: cores do texto (normal, hover/pressionado).
            borda: cor da borda.
            **opcoes: opções extras do estilo (fonte, espaçamento...).
        """
        normal, hover, pressionado = fundo
        estados_fundo = [
            ("disabled", Cores.FUNDO),
            ("pressed", pressionado),
            ("active", hover),
        ]
        estilo = ttk.Style(self)
        estilo.configure(
            nome,
            background=normal,
            foreground=texto[0],
            bordercolor=borda,
            focuscolor=texto[0],
            relief="solid",
            **opcoes,
        )
        estilo.map(
            nome,
            relief=[("", "solid")],
            background=estados_fundo,
            lightcolor=estados_fundo,
            darkcolor=estados_fundo,
            foreground=[
                ("disabled", Cores.TEXTO_DESATIVADO),
                ("pressed", texto[1]),
                ("active", texto[1]),
            ],
            bordercolor=[("disabled", Cores.BORDA), ("pressed", pressionado), ("active", hover)],
            focuscolor=[("pressed", texto[1]), ("active", texto[1])],
        )

    # -- Construção da interface --------------------------------------------

    def _montar_interface(self) -> None:
        conteudo = ttk.Frame(self, padding=24)
        conteudo.grid(row=0, column=0, sticky="nsew")
        conteudo.columnconfigure(0, weight=1, minsize=LARGURA_MINIMA)

        self._criar_cabecalho(conteudo).grid(row=0, sticky="ew", pady=(0, 20))
        self._criar_formulario(conteudo).grid(row=1, sticky="ew")
        self._criar_painel_resultado(conteudo).grid(row=2, sticky="ew", pady=(16, 20))
        self._criar_rodape(conteudo).grid(row=3, sticky="ew")

    def _criar_cabecalho(self, pai: tk.Misc) -> tk.Frame:
        cartao = tk.Frame(
            pai,
            background=Cores.FUNDO,
            highlightthickness=2,
            highlightbackground=Cores.CIANO,
            padx=16,
            pady=14,
        )
        ttk.Label(cartao, text="CONVERSOR DE BASES NUMÉRICAS", style="Titulo.TLabel").pack()
        ttk.Label(
            cartao,
            text="Exercício 37 🐍  ·  Bons estudos em Python",
            style="Subtitulo.TLabel",
        ).pack(pady=(4, 0))
        return cartao

    def _criar_formulario(self, pai: tk.Misc) -> ttk.Frame:
        formulario = ttk.Frame(pai)
        formulario.columnconfigure(0, weight=1)

        ttk.Label(formulario, text="NÚMERO INTEIRO", style="Legenda.TLabel").grid(
            row=0, sticky="w"
        )
        self._campo_numero = ttk.Entry(
            formulario,
            textvariable=self._texto_numero,
            font=self._fonte_numero,
            justify="center",
            width=1,  # a largura real vem do layout (sticky="ew")
        )
        self._campo_numero.grid(row=1, sticky="ew", pady=(6, 0))

        # Linha reservada para mensagens de erro (evita que o layout "pule").
        ttk.Label(formulario, textvariable=self._erro, style="Erro.TLabel").grid(
            row=2, sticky="w", pady=(4, 8)
        )

        ttk.Label(formulario, text="CONVERTER PARA", style="Legenda.TLabel").grid(
            row=3, sticky="w"
        )
        seletor = ttk.Frame(formulario)
        seletor.grid(row=4, sticky="ew", pady=(6, 18))
        for coluna, sistema in enumerate(SistemaNumerico):
            seletor.columnconfigure(coluna, weight=1, uniform="sistemas")
            ttk.Radiobutton(
                seletor,
                text=sistema.rotulo,
                value=sistema.name,
                variable=self._sistema,
                command=self._exibir_resultado,
                style="Segmento.Toolbutton",
            ).grid(row=0, column=coluna, sticky="ew")

        ttk.Button(
            formulario,
            text="Converter",
            style="Primario.TButton",
            command=self._converter,
        ).grid(row=5, sticky="ew")
        return formulario

    def _criar_painel_resultado(self, pai: tk.Misc) -> tk.Frame:
        painel = tk.Frame(
            pai,
            background=Cores.FUNDO,
            highlightthickness=1,
            highlightbackground=Cores.BORDA,
            padx=16,
            pady=12,
        )
        painel.columnconfigure(0, weight=1)

        ttk.Label(painel, textvariable=self._legenda, style="Legenda.TLabel").grid(
            row=0, column=0, columnspan=2, sticky="w"
        )
        ttk.Entry(
            painel,
            textvariable=self._resultado,
            state="readonly",
            font=self._fonte_resultado,
            style="Resultado.TEntry",
            width=1,
        ).grid(row=1, column=0, sticky="ew", pady=(6, 0))

        self._botao_copiar = ttk.Button(
            painel,
            text="Copiar",
            width=10,  # largura fixa: o texto muda para "Copiado ✓"
            style="Secundario.TButton",
            command=self._copiar_resultado,
        )
        self._botao_copiar.grid(row=1, column=1, sticky="e", padx=(12, 0), pady=(6, 0))
        return painel

    def _criar_rodape(self, pai: tk.Misc) -> ttk.Frame:
        rodape = ttk.Frame(pai)
        rodape.columnconfigure(0, weight=1)

        tk.Frame(rodape, height=1, background=Cores.BORDA).grid(
            row=0, column=0, columnspan=2, sticky="ew", pady=(0, 14)
        )
        ttk.Label(rodape, text="Obrigado por praticar! 🐍", style="Discreto.TLabel").grid(
            row=1, column=0, sticky="w"
        )
        ttk.Button(rodape, text="Sair", style="Perigo.TButton", command=self.destroy).grid(
            row=1, column=1, sticky="e"
        )
        return rodape

    def _registrar_eventos(self) -> None:
        # Enter (principal ou do teclado numérico) também converte.
        self.bind("<Return>", lambda _evento: self._converter())
        self.bind("<KP_Enter>", lambda _evento: self._converter())
        self._texto_numero.trace_add("write", self._ao_editar_numero)

    def _centralizar_janela(self) -> None:
        """Posiciona a janela no centro horizontal e no terço superior da tela."""
        self.update_idletasks()
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) // 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) // 3
        self.geometry(f"+{x}+{y}")  # só a posição: o tamanho segue o conteúdo

    # -- Ações --------------------------------------------------------------

    def _converter(self) -> None:
        """Valida o número digitado e exibe a conversão."""
        texto = self._texto_numero.get().strip()
        if not texto:
            self._mostrar_erro("Digite um número para converter.")
            return

        try:
            numero = int(texto)
        except ValueError:
            if texto.lstrip("+-").isdigit():
                # O Python limita a conversão de textos com mais de 4300 dígitos.
                self._mostrar_erro("Número grande demais para converter.")
            else:
                self._mostrar_erro("Número inválido. Use apenas inteiros, como 255 ou -42.")
            return

        self._numero = numero
        self._exibir_resultado()

    def _exibir_resultado(self) -> None:
        """Atualiza o painel de resultado conforme o número e o sistema atuais."""
        if self._numero is None:
            self._legenda.set("RESULTADO")
            self._resultado.set("")
            self._botao_copiar.state(["disabled"])
            return

        sistema = SistemaNumerico[self._sistema.get()]
        self._legenda.set(f"RESULTADO EM {sistema.rotulo.upper()} (BASE {sistema.base})")
        self._resultado.set(converter_numero(self._numero, sistema))
        self._botao_copiar.state(["!disabled"])

    def _mostrar_erro(self, mensagem: str) -> None:
        self._numero = None
        self._exibir_resultado()
        self._erro.set(mensagem)
        self._campo_numero.state(["invalid"])
        self._campo_numero.focus_set()

    def _ao_editar_numero(self, *_args: object) -> None:
        """Limpa erro e resultado anterior assim que o número é alterado."""
        self._erro.set("")
        self._campo_numero.state(["!invalid"])
        self._numero = None
        self._exibir_resultado()

    def _copiar_resultado(self) -> None:
        """Copia o resultado para a área de transferência e dá um retorno visual."""
        resultado = self._resultado.get()
        if not resultado:
            return

        self.clipboard_clear()
        self.clipboard_append(resultado)

        self._botao_copiar.configure(text="Copiado ✓")
        if self._aviso_copia_id is not None:
            self.after_cancel(self._aviso_copia_id)
        self._aviso_copia_id = self.after(DURACAO_AVISO_COPIA, self._restaurar_botao_copiar)

    def _restaurar_botao_copiar(self) -> None:
        self._aviso_copia_id = None
        self._botao_copiar.configure(text="Copiar")


def main() -> None:
    """Ponto de entrada do programa."""
    app = ConversorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
