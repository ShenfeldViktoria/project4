def zamina(array):
    if len(array) % 2 != 0:
        print("Масив повинен мати парну кількість елементів")
        return

    mid = len(array) // 2

    array[:mid], array[mid:] = array[mid:], array[:mid]

if __name__ == "__main__":
    my_array = [4, 2, 7, 10, 5, 6]
    print("Оригінальний масив ", my_array)

    zamina(my_array)
    print("Масив після заміни ", my_array)
