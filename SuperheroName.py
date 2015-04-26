letter = {'a': 'Captain', 'b': 'X', 'c':'Flash', 'd':'Doctor', 'e': 'Exuberant', 'f': 'Super', 'g':'Fire', 'h':'Green', 'i':'Ogre', 'j':'Incredible', 'k':'Amazing', 'l':'The', 'm':'Marvelous', 'n':'Red', 'o':'Invisible', 'p':'Mr.', 'q':'Water', 'r':'Magnificent', 's':'The Great', 't':'Fantastic', 'u':'Wonder', 'v':'Blue', 'w':'Tiny', 'x':'Yellow', 'y':'Fabulous', 'z':'Stupid'}
first_Name = raw_input('Enter your first name:')
first_Name = first_Name.lower()
first_Letter = first_Name [0]
#print first_Letter


let = {'a': 'Underpants', 'b': 'Women/Man', 'c':'Pumpkin', 'd':'Lantern', 'e': 'Murica', 'f': 'Canada', 'g':'giraffe', 'h':'Coder', 'i':'Ogre', 'j':'Hulk', 'k':'Flame', 'l':'Morgan', 'm':'Potato', 'n':'Hawk', 'o':'Pants', 'p':'Cheetah', 'q':'Emu', 'r':'Fly', 's':'Police', 't':'Monkey', 'u':'Thrasher', 'v':'Warrior', 'w':'General', 'x':'Computer', 'y':'Sparrow', 'z':'Charmander'}
last_Name = raw_input('Enter your last name:')
last_Name = last_Name.lower()
last_Letter = last_Name [0]
#print last_Letter
print let[last_Letter] + letter[first_Letter]
