import pandas as pd
def do(result,test):
	# Write the test results 
	output = pd.DataFrame(data={"id":test["id"], "type":result})
	output.to_csv( "result.csv", index=False, quoting=3 )