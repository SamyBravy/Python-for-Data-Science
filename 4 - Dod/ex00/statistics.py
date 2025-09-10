from typing import Any


def mean(numbers):
	return sum(numbers) / len(numbers)

def median(numbers):
	numbers = sorted(numbers)
	l = len(numbers)

	if l % 2 == 1:
		return numbers[l // 2]
	else:
		return mean(numbers[l // 2 - 1], numbers[l // 2])

def quartile(numbers):
	numbers = sorted(numbers)
	l = len(numbers)

	pos = l / 4
	if isinstance(pos, int):
		q1 = numbers[pos]
	else:
		q1 = mean([numbers[int(pos) - 1], numbers[int(pos)]])

	pos = 3 * l / 4
	if isinstance(pos, int):
		q2 = numbers[pos]
	else:
		q2 = mean([numbers[int(pos) - 1], numbers[int(pos)]])

	return [q1, q2]

def check_validity(numbers):
	if len(numbers) == 0:
		print("ERROR")
		return False

	if not all(type(n) in [int, float] for n in numbers):
		print("ERROR")
		return False

	return True

def ft_statistics(*args: Any, **kwargs: Any) -> None:
	for _, op in kwargs.items():
		match op:
			case "mean":
				if not check_validity(args):
					continue
				print("mean : ", mean(args))
			case "median":
				if not check_validity(args):
					continue
				print("median : ", median(args))
			case "quartile":
				if not check_validity(args):
					continue
				print("quartile : ", quartile(args))
			#case "std":
			#	print("std : ", std(args))
			#case "var":
			#	print("var : ", var(args))
