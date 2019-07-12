import datetime
import warnings
def create_header (authors_list,place="Paris"):
    """Creates the header text based on  the authors list
   
    Parameters
    ----------
    authors_list : a list of dictionnaries
        each dict should have "firstname" and "lastname" keys
       
    Returns
    -------
    header_text : str
      the header text
     
    Note
    ----
    date is updated at the function execution time
    """
    today=datetime.date.today()
   
    ligne1=f'{place}, le {today.day}/{today.month:02d}/{today.year}\n\n### auteur(s) :\n'
    lignes=[ligne1]
    #get the authors names
    for aut in authors_list:
        try:
            firstname2=aut['firstname']
        except KeyError: #met XXX si firstname is missing, utile pour afficher le message firstname is missing
            firstname2='XXX'
            warnings.warn('First Name is missing')
            print('Firstname missing')

        lastname2=aut.get('lastname',"XXX") #met XXX si lastname is missing
        lignes.append(f'- {firstname2} {lastname2}')
   
    return "\n".join(lignes)