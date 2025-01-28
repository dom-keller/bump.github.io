import pandas as pd
import json

data = [{"Name":"Alexa Grossman","Email":"alexagrossman@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Alexander Rashedi","Email":"arashedi@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Andrew Marquette","Email":"Andrew.Marquette@ufl.edu","Mentor Meeting 3":"u","Retreat":""},{"Name":"Andrew Petrousky","Email":"andrew.petrousky@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Annalee Watts","Email":"annalee.watts@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Ashley Lane","Email":"ashleylane@ufl.edu","Mentor Meeting 3":"x","Retreat":"e"},{"Name":"Ava Mariani","Email":"avamariani@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Benjamin Keim","Email":"bkeim@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Braden Urso","Email":"bradenurso@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Brooke Reeves","Email":"brookereeves@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Brooke Zaremskas","Email":"zaremskasbrooke@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Caroline Acosta","Email":"carolineacosta@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Dalya Mawlawi","Email":"dmawlawi@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Daniel Shumway","Email":"Daniel.shumway@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"David Hayes","Email":"davidhayes1@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Enslie Lloyd","Email":"e.lloyd@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Gabriela Dos Santos","Email":"gabriela.dossant@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Griffin Olecki","Email":"griffin.olecki@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Ithan Ash","Email":"ithanash@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Izabella Kelly","Email":"izabellakelly@ufl.edu","Mentor Meeting 3":"u","Retreat":""},{"Name":"Jillian Cranney","Email":"cranneyj@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Jordyn Klein","Email":"jordynklein@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Juniper Nguyen","Email":"duyen.nguyen@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Kasey Lane","Email":"kaseylane@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Katherine McKeon","Email":"katherinemckeon@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Katie Troilo","Email":"katietroilo@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Kelly Chen","Email":"kchen2@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Kennedy Weissman","Email":"weissmank@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Khalin Pudupakkam","Email":"khalinpudupakkam@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Kylie Leung","Email":"leung.kylie@ufl.edu","Mentor Meeting 3":"x","Retreat":"e"},{"Name":"Liam Farrell","Email":"l.farrell@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Lila Patterson","Email":"ln.patterson@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Lilah Edwards","Email":"lilah.edwards@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Lindsey Davis","Email":"lindseydavis@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Lola Plasencia","Email":"l.plasencia@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Luke Higgins","Email":"luke.higgins@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Margaret Rowan","Email":"margaret.rowan@ufl.edu","Mentor Meeting 3":"u","Retreat":""},{"Name":"Maryam Elfakir","Email":"maryam.elfakir@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Mason Matos","Email":"mmatos1@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Michelle Ojala","Email":"m.ojala@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Morgan Tafel","Email":"m.tafel@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Nicolas Sanders","Email":"sanders.n@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Nikolas Lima","Email":"nikolas.lima@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Oriana Rodriguez","Email":"rodriguezoriana@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Reese Biggerstaff","Email":"reesebiggerstaff@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Richard King","Email":"kingrichard@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Robert St Pierre","Email":"stpierrer@ufl.edu","Mentor Meeting 3":"u","Retreat":""},{"Name":"Ross Bloecker","Email":"rbloecker@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Sammi Lin","Email":"sammi.lin@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Sofia Triana","Email":"sofiatriana@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Sofia Yaffar","Email":"syaffar@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Sonakshi Srivastava","Email":"ssrivastava1@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Sophia Palmeiro","Email":"spalmeiro@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Sophie Heidt","Email":"sophieheidt@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Sum Ye (Priscilla) Poon","Email":"spoon1@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Taylor Aks","Email":"taylor.aks@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Taylor Benson","Email":"taylorbenson@ufl.edu","Mentor Meeting 3":"u","Retreat":""},{"Name":"Thomas Montobbio","Email":"thomasmontobbio@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Tiffany Moliver","Email":"tiffanymoliver@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Timon Dietrich","Email":"dietricht@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Trent Burger","Email":"t.burger@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Victoria Cannata","Email":"victoria.cannata@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"Victoria Rios Narvaez","Email":"vriosnarvaez@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Yoni Mann","Email":"jonathan.mann@ufl.edu","Mentor Meeting 3":"e","Retreat":""},{"Name":"Zoe Capponi","Email":"zcapponi@ufl.edu","Mentor Meeting 3":"x","Retreat":""},{"Name":"","Email":"","Mentor Meeting 3":"49","Retreat":"0"},{"Name":"","Email":"","Mentor Meeting 3":"11","Retreat":"2"},{"Name":"","Email":"","Mentor Meeting 3":"5","Retreat":"0"}]

df = pd.DataFrame(data)
print(df)
