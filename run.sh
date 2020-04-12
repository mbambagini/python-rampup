#! /bin/sh

simple_test() {
  echo "######################################"
  echo "# Running $1"
  python $1
}

test_integer_input() {
  echo "######################################"
  echo "# Running $1"
  tmpFilename="tmp_file_run_$1.txt"
  echo 10 > $tmpFilename
  python $1 < $tmpFilename
  rm $tmpFilename
}

test_with_teardown() {
  echo "######################################"
  echo "# Running $1"
  python $1
  rm $2
}

simple_test 01_helloworld.py
simple_test 02_basictypes.py
simple_test 03_lists.py
simple_test 04_dictionaries.py
test_integer_input 05_input.py
simple_test 06_while_and_if.py
simple_test 07_functions.py
simple_test 08_classes.py
simple_test 09_import.py
test_with_teardown 10_files.py temp.txt
test_with_teardown 11_json.py animal.txt
simple_test 12_exceptions.py
simple_test 13_test.py


