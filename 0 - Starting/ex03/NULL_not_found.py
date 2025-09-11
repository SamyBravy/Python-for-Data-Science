def NULL_not_found(object: any) -> int:
	match object:
		case None:
			print("Nothing: None", end=' ')
		case float():
			if str(object) == "nan":
				print("Cheese: nan", end=' ')
			else:
				print("Type not Found")
				return 1
		case False:
			print("Fake: False", end=' ')
		case 0:
			print("Zero: 0", end=' ')
		case '':
			print("Empty:", end=' ')
		case _:
			print("Type not Found")
			return 1
	print(type(object))
	return 0