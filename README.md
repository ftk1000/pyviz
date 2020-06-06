# pyviz
python visualization tricks

2020.05.16


…or create a new repository on the command line

    echo "# pyviz" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/ftk1000/pyviz.git
    git push -u origin master
                
…or push an existing repository from the command line

    git remote add origin https://github.com/ftk1000/pyviz.git
    git push -u origin master

…or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

# Tips
[Draw a circle](https://stackoverflow.com/questions/9215658/plot-a-circle-with-pyplot)<br>
[Add a colorbar-1](https://stackoverflow.com/questions/45020583/python-3-adding-a-colorbar-with-matplotlib)<br>
[Add a colorbar-2](https://stackoverflow.com/questions/25505674/python-matplotlib-add-colorbar)<br>
[marker="^", s=10](https://stackoverflow.com/questions/19451400/matplotlib-scatter-marker-size)<br>

        #generate a list of markers and another of colors 
        markers = ["." , "," , "o" , "v" , "^" , "<", ">"]
        colors = ['r','g','b','c','m', 'y', 'k']

[viewing-all-defined-variables](https://stackoverflow.com/questions/633127/viewing-all-defined-variables)<br>

        dir()     # will give you the list of in scope variables:
        globals() # will give you a dictionary of global variables
        locals()  # will give you a dictionary of local variables
        %who      # list of all current user-defined variables
        %whos     # same with more details
        for name in vars().keys():
            print(name)
        for value in vars().values():
            print(value)
        
[]()<br>
[]()<br>
[]()<br>
[]()<br>
