# To generate the results without
# constraints is necessary to modify
# the file ../evaluate.py (rename the function
# without constraints as "Evaluate")
# and run
sh doit.sh output.txt
awk -f p.awk output.txt


# To generate the results with
# constraints, modify
# the file ../evaluate.py (rename the function
# without constraints as "Evaluate1", and the 
# function with the constraint as "Evaluate"
# and run
sh doit.sh outputConst.txt
awk -f pConst.awk output.txt

