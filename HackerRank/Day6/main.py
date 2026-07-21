import sys
from typing import List, Tuple

class StringSplitter:
    """Clase encargada de procesar cadenas separando sus índices pares e impares."""

    @staticmethod
    def process_string(s: str) -> Tuple[str, str]:
        """
        Separa una cadena en dos partes: caracteres en posiciones pares e impares.

        Args:
            s (str): Cadena de texto a procesar.

        Returns:
            Tuple[str, str]: Tupla con (caracteres_pares, caracteres_impares).
        """
        return s[::2], s[1::2]

    @classmethod
    def process_batch(cls, strings: List[str]) -> List[Tuple[str, str]]:
        """Procesa una lista completa de cadenas de texto."""
        return [cls.process_string(s) for s in strings]


class InputHandler:
    """Clase encargada de la lectura y validación de datos de entrada."""

    @staticmethod
    def read_from_stdin() -> List[str]:
        """
        Lee todas las líneas desde la entrada estándar y valida su formato.

        Returns:
            List[str]: Lista de cadenas a procesar.

        Raises:
            ValueError: Si la entrada está vacía o el formato de T es inválido.
        """
        raw_input = sys.stdin.read().split()
        if not raw_input:
            raise ValueError("No se proporcionó ningún dato de entrada.")

        try:
            t = int(raw_input[0])
        except ValueError:
            raise ValueError("El primer valor de entrada debe ser un número entero (T).")

        data = raw_input[1:]
        if len(data) < t:
            raise ValueError(f"Se esperaban {t} cadenas, pero solo se recibieron {len(data)}.")

        return data[:t]


def main() -> None:
    """Punto de entrada principal de la aplicación."""
    try:
        strings_to_process = InputHandler.read_from_stdin()
        results = StringSplitter.process_batch(strings_to_process)

        # Presentación limpia de resultados
        for pares, impares in results:
            print(f"{pares} {impares}")

    except ValueError as err:
        print(f"Error de validación: {err}", file=sys.stderr)
        sys.exit(1)
    except Exception as err:
        print(f"Error inesperado: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()