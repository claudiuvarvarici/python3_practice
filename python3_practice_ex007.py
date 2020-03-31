def ex():
  file_name=input("Input a filename followed by an extention: ")
  print(file_name)
  f_exten=file_name.split(".")
  print("filename: ", f_exten[0])
  print("extension: ", f_exten[-1])

ex()
