from pyscript import display, document

def student_candidate(e):
    document.getElementById('output').innerHTML = ' '
    first_name = document.getElementById('student_firstname').value
    last_name = document.getElementById('student_lastname').value

    volleyball_team = ['Poppy' + 'Yeng', 'Aster' + 'Kitchie', 'Caspian' + 'Jhene', 'Zinnia' + 'Niki']
    member_checker = first_name + last_name in volleyball_team 

    display_message = (f'Sorry, you are not in the team', f'Congratulations {first_name +  last_name} you are now in the OBMC volleyball varsity! ')
    
    display(display_message[member_checker], target='output')

def fullname(e):
    document.getElementById('output').innerHTML = ' '
    first_name = document.getElementById('firstname').value
    last_name = document.getElementById('lastname').value

    full_name = first_name + last_name

    grade7 = {'Mikasa Ackerman', 'Eren Yeager', 'Armin Arlert', 'Hange Zoe', 'Levi Ackerman'}
    grade7.add(first_name + last_name)
    display(grade7, target='output') 

    display_message =(f'Total number of members = : 6')
    display(display_message, target='output')

def check_element(e):
    document.getElementById('output').innerHTML = ' '
    element = document.getElementById('symbol_input').value

    non_metals = {
        'H': 'Hydrogen, 1, 1.008',
        'C': 'Carbon, 6, 12.011',
        'O': 'Oxygen, 8, 15.999',
        'N': 'Nitrogen, 7, 14.007',
        'P': 'Phosphorus, 15, 30.974',
        'S': 'Sulfur, 16, 32.06',
        'Se': 'Selenium, 34, 78.96',
        'F': 'Flourine, 9, 18.998',
        'Cl': 'Chlorine, 17, 35.45',
        'Br': 'Bromine, 35, 79.904',
        'I': 'Iodine, 53, 126.904',
        'At': 'Astatine, 85, 210',
        'He': 'Helium, 2, 4.0026',
        'Ne': 'Neon, 10, 20.180',
        'Ar': 'Argon, 18, 39.95',
        'Kr': 'Krypton, 36, 83.798',
        'Xe': 'Xenon, 54, 131.293',
        'Rn': 'Radon, 86, 222',
        'Ts': 'Tennessine, 117, 294',
        'Og': 'Oganesson, 118, 294'
    }
   
    element_checker = element in non_metals

    display_message = (f'Sorry, that is not a nonmetal', f'That is a nonmetal')

    hydrogen_checker = 'H' in element
    hydro_message = (f' ', f'{non_metals.get('H')}')

    display (hydro_message[hydrogen_checker], target='output')

    carbon_checker = 'C' in element
    c_message = (f' ', f'{non_metals.get('C')}')
    
    display (c_message[carbon_checker], target='output')

    oxygen_checker = 'O' in element
    o_message = (f' ', f'{non_metals.get('O')}')
        
    display (o_message[oxygen_checker], target='output')

    nitrogen_checker = 'N' in element
    n_message = (f' ', f'{non_metals.get('N')}')
    
    display (n_message[nitrogen_checker], target='output')
    
    phos_checker = 'P' in element
    p_message = (f' ', f'{non_metals.get('P')}')
        
    display (p_message[phos_checker], target='output')
    
    sulfur_checker = 'S' in element
    s_message = (f' ', f'{non_metals.get('S')}')
            
    display (s_message[sulfur_checker], target='output')

    selenium_checker = 'Se' in element
    sel_message = (f' ', f'{non_metals.get('Se')}')
    
    display (sel_message[selenium_checker], target='output')
    
    fluorine_checker = 'F' in element
    fl_message = (f' ', f'{non_metals.get('F')}')
        
    display (fl_message[fluorine_checker], target='output')
    
    chl_checker = 'Cl' in element
    ch_message = (f' ', f'{non_metals.get('Cl')}')
            
    display (ch_message[chl_checker], target='output')
    
    bromine_checker = 'Br' in element
    br_message = (f' ', f'{non_metals.get('Br')}')
        
    display (br_message[bromine_checker], target='output')
        
    iodine_checker = 'I' in element
    i_message = (f' ', f'{non_metals.get('I')}')
            
    display (i_message[iodine_checker], target='output')
        
    astatine_checker = 'At' in element
    a_message = (f' ', f'{non_metals.get('At')}')
                
    display (a_message[astatine_checker], target='output')

    helium_checker = 'He' in element
    he_message = (f' ', f'{non_metals.get('He')}')
    
    display (he_message[helium_checker], target='output')
    
    neon_checker = 'Ne' in element
    neo_message = (f' ', f'{non_metals.get('Ne')}')
        
    display (neo_message[neon_checker], target='output')
    
    argon_checker = 'Ar' in element
    ar_message = (f' ', f'{non_metals.get('Ar')}')
            
    display (ar_message[argon_checker], target='output')
    
    krypton_checker = 'Kr' in element
    kr_message = (f' ', f'{non_metals.get('Kr')}')
        
    display (kr_message[krypton_checker], target='output')
        
    xenon_checker = 'Xe' in element
    x_message = (f' ', f'{non_metals.get('Xe')}')
            
    display (x_message[xenon_checker], target='output')
        
    radon_checker = 'Rn' in element
    r_message = (f' ', f'{non_metals.get('Rn')}')
                
    display (r_message[radon_checker], target='output')

    tennessine_checker = 'Ts' in element
    t_message = (f' ', f'{non_metals.get('Ts')}')
                    
    display (t_message[tennessine_checker], target='output')

    oganesson_checker = 'Og' in element
    og_message = (f' ', f'{non_metals.get('Og')}')
                    
    display (og_message[oganesson_checker], target='output')

    
    display(display_message[element_checker], target='output') 
