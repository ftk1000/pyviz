# [Kalman_filter.md](https://github.com/ftk1000/pyviz/blob/master/Kalman_filter.md)<br>
# [3D_surface.md](https://github.com/ftk1000/pyviz/blob/master/3D_surface.md)<br>

# pyviz - python visualization tricks
[Visualization with Matplotlib on COLAB: github/jakevdp/PythonDataScienceHandbook](https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.00-Introduction-To-Matplotlib.ipynb#scrollTo=TZGGO5cuCvXL)<br>
<br>
[2019: HABR: Другой GitHub: репозитории по Data Science, визуализации данных и глубокому обучению](https://habr.com/ru/company/mailru/blog/437940/)<br>
[2019: HABR: группировки и визуализации данных в Python](https://habr.com/ru/company/mailru/blog/445834/)<br>
[2018: Визуализация данных для вашего Web-проекта](https://habr.com/ru/company/dataart/blog/417947/)<br>
[2017:YT: How to Make a Google Map from Excel ](https://www.youtube.com/watch?v=SLMzhOoA29M)<br>
[]()<br>

[2016: Jason Brownlee: Visualize Machine Learning Data in Python With Pandas](https://machinelearningmastery.com/visualize-machine-learning-data-python-pandas/)<br>
  - data.hist(),  
  - data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
  - data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
  - data.corr()
  - scatter_matrix(data)
[]()<br>
[]()<br>
[]()<br>
[]()<br>


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

=============================

### MATLAB options
[2016: YT: MATLAB Live Editor DEMO](https://www.youtube.com/watch?v=jI56Qe1tLFQ)<br>
[MATLAB Self-Paced Courses](https://matlabacademy.mathworks.com/)<br>
[MATLAB Webinar: signal-processing-and-machine-learning-techniques-for-sensor-data-analytics](https://www.mathworks.com/videos/signal-processing-and-machine-learning-techniques-for-sensor-data-analytics-107549.html)<br>
[2019: YT: Using MATLAB with Python](https://www.youtube.com/watch?v=y7NBT6O0fJU)<br>
[]()<br>
[Webinar: matlab-with-python](https://www.mathworks.com/videos/using-matlab-with-python-1591216182793.html?s_v1=34589&elqem=3252609_EM_NA_LWB_20-12_USING-MATLAB-WITH-PYTHON_POST&s_tid=srchtitle&elqTrackId=1da6d415d924424089b870296c5d332b&elq=5de7df4ea60e4e29b3690978264ee642&elqaid=34589&elqat=1&elqCampaignId=12552)<br>
[]()<br>


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
