""" Consider a database table, Emails, which has the attributes First Name and Email ID.
Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com."""
if __name__ == '__main__':
  N = int(input().strip())
  List_name = []

  for N_itr in range(N):
    first_multiple_input = input().rstrip().split()

    firstName = first_multiple_input[0]

    emailID = first_multiple_input[1]
        
    if emailID.endswith('@gmail.com'):
      List_name.append(firstName)
    
    List_name.sort()
    for i in List_name:
      print(i)     
