def union(set1, set2):
  return set1.union(set2)


def intersection(set1, set2):
  return set1.intersection(set2)


def difference(set1, set2):
  return set1.difference(set2)


def cartesian_product(set1, set2):
  return {(x, y) for x in set1 for y in set2}


def perform_operation(operation, set1, set2):
  if operation == 'U':
    result = union(set1, set2)
    operation_desc = "União"
  elif operation == 'I':
    result = intersection(set1, set2)
    operation_desc = "Interseção"
  elif operation == 'D':
    result = difference(set1, set2)
    operation_desc = "Diferença"
  elif operation == 'C':
    result = cartesian_product(set1, set2)
    operation_desc = "Produto Cartesiano"

  return operation_desc, set1, set2, result


def main():
  input_file = input("Digite o nome do arquivo de entrada: ")

  with open(input_file, 'r') as file:
    num_operations = int(file.readline().strip())

    for _ in range(num_operations):
      operation = file.readline().strip()
      set1 = set(file.readline().strip().split(', '))
      set2 = set(file.readline().strip().split(', '))

      operation_desc, set1_desc, set2_desc, result = perform_operation(
          operation, set1, set2)

      print(
          f"{operation_desc}: conjunto 1 {{{', '.join(set1_desc)}}}, conjunto 2 {{{', '.join(set2_desc)}}}. Resultado: {{{', '.join(result)}}}"
      )


if __name__ == "__main__":
  main()
