from typing import Iterable


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for idx, item in enumerate(lst, 1):  # idx parte da 1, comodo per le percentuali
        # (qui poi aggiungeremo l'aggiornamento della barra)
        yield item
    print()
