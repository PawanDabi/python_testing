import doctest
def student_info(fname,lname,id,branch,school_name):
    """
    this functons returns the student informations
    """
    print(f"your name: {fname}\nlast name: {lname}\nyour id: {id}\nyour branch: {branch}\nschool name: {school_name}")

if __name__ == "__main__":
    doctest.testfile("test_case.txt",verbose=True)