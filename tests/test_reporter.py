from reporter import header

def test_reporter():
    assert True

   
def test_create_header():
    author = {
        'firstname': 'Miles',
        'lastname' : 'Davis'
        
    }

    author2 = {
        'firstname': 'John',
        'lastname' : 'Coltrane'
        
    }
    authors=[author,author2]
    header_texte = header.create_header(authors)

    assert len(header_texte)>0
 
    assert 'Miles' in header_texte