def ft_tqdm(lst: range) -> None:
    """Displays a progress bar in the terminal while iterating over a list."""

    if len(lst) == 0:
        return

    bar_len = 102
    for i in range(len(lst)):
        part = i / len(lst)
        perc = round(part * 100)
        print(f"\r{perc:3d}%", end='')

        filled = round(part * bar_len)
        bar = '█' * filled + ' ' * (bar_len - filled)
        print(f"|{bar}", end='')

        print(f"| {i}/{len(lst)}", end='')
        yield lst[i]

    print(f"\r100%|{'█' * 102}| {len(lst)}/{len(lst)}")
