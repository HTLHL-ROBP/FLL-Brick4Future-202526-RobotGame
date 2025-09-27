from pybricks.tools import hub_menu


def menu() -> None:
	selected_run: int | str = hub_menu(1, 2, 3)

	match selected_run:
		case 1:
			print("Starting Run 1...")
		case 2:
			print("Starting Run 2...")
		case 3:
			print("Starting Run 3...")


if __name__ == "__main__":
	menu()
