import doctest
def square(n:int)->int:
    """
    Returns the square of a number.

    >>> square(2)
    4
    >>> square(-3)
    9
    >>> square(0)
    0
    >>> square(10)
    100
    """
    return n * n


# testing on multiple functions
def informations(first_name, last_name, age):
   '''
    Returns the informations of person

   >>> informations("ajay","pathak",44)
   your first name is: ajay, last name is: pathak and age is: 44

   >>> informations("sanjay","lila",56)
   your first name is: sanjay, last name is: lila and age is: 56

   >>> informations("rohan","pandey",14)
   your first name is: rohan, last name is: pandey and age is: 14
   '''
   print(f"your first name is: {first_name}, last name is: {last_name} and age is: {age}")

def student_info(fname,lname,id,branch,school_name):
    '''
    this functions returns the student informations
    
    >>> student_info("sohan","verma",123121,"pcm","svnhss")
    your name: sohan
    last name: verma
    your id: 123121
    your branch: pcm
    school name: svnhss

    >>> student_info("abhishek","joshi",123122,"pcm","gvmhss")
    your name: abhishek
    last name: joshi
    your id: 123122
    your branch: pcm
    school name: gvmhss

    '''
    print(f"your name: {fname}\nlast name: {lname}\nyour id: {id}\nyour branch: {branch}\nschool name: {school_name}")
if __name__ == "__main__":
    find_method=doctest.DocTestFinder()
    run_method=doctest.DocTestRunner()
    for test_cases in find_method.find(student_info):
        print(f"Running tests for: {test_cases.name}")
        result = run_method.run(test_cases, clear_globs=False) 

        print(f"Tests run: {result.attempted}, Failures: {result.failed}")
        print("-" * 40)
   
