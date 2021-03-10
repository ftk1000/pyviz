# ANNOTATION 
[different-colors-in-the-same-annotate](https://stackoverflow.com/questions/24108063/matplotlib-two-different-colors-in-the-same-annotate)<br>
[]()<br>
[]()<br>

## [Create Beautiful Architecture Diagrams with Python](https://towardsdatascience.com/create-beautiful-architecture-diagrams-with-python-7792a1485f97)

## Graph Viz Tools: Gephi, Cytoscape, NodeXL, GraphViz, mermaid, networkX, igraph, Jgraph

            Semyon Sinchenko: Если для целей "просто посмотреть", то я бы предложил Gephi - там все это (Лоувэйн, 
            Пэйдж Ранк, Форс Атлас 2 и т.д.) делается мышкой, при этом он вполне быстр, а потом 
            можно будет для прода просто воспользоваться его API. Единственное - он под GPL идет, это надо учитывать.
            
            JGraphT. Я много юзал и по мне это лучшее (из либ под не GPL лицензиями) для "прода", 
            хотя я бы не сказал, что она прямо мега мощная. Она просто по возрасту старше IGraph 
            мне кажется, там есть целое море всяких алгоритмов, которые фиг где найдешь (остовные 
            деревья, раскраски, изоморфизм и т.д.) и она мега-стабильная. Для графов с типами Int для 
            вершин и ребер там есть https://jgrapht.org/javadoc/org.jgrapht.opt/org/jgrapht/opt/graph/fastutil/FastutilMapIntVertexGraph.html 
            который быстр и хорош по памяти, но в целом C++ либы будет значимо быстрее. 
            JGraphT это больше про энтерпрайз и стабильность.

* [Gephi - The Open Graph Viz Platform](https://github.com/gephi/gephi)<br>

            an award-winning open-source platform for visualizing and manipulating large graphs. 
            Sviatoslav Iguana (@IggiSv9t  Святослав мастер визуализаций): В Gephi всё есть. 
            Там можно размазать сильнее вершины через Yifan Hu после какого-нибудь стандартного 
            Force Atlas, настроить раскраску по атрибутам и потом в меню экспорта уже допилить 
            все детали внешнего вида.Tам просто нужно двигать ползунки и смотреть, что выходит. 
            Если через API то больше возни получится.

* [https://github.com/mermaid-js/mermaid](https://github.com/mermaid-js/mermaid)<br>

            Mermaid is a Javascript based diagramming and charting tool that uses 
            Markdown-inspired text definitions and a renderer to create and modify 
            complex diagrams. The main purpose of Mermaid is to help documentation 
            catch up with development.
            
* [kaggle.com/alexandervc/igraph-cheatsheet](https://www.kaggle.com/alexandervc/igraph-cheatsheet)            

            Все библиотеки схожи по интерфейсу, просто нетворкХ написан на самом Питоне - 
            поэтому медленный, но везде работает. Играф - написан на С, поэтому быстрый, 
            но могут быть проблемы с тем чтобы его инсталировать - на каггле - он просто уже есть. 
            На колаб без проблем ставится. Но бывают проблемы - например на нанохаб.
            Еще одна тупая проблема с нетворкХ - если вам надо нарисать граф у которго есть селф-лупы - 
            то НИКАК НЕЛЬЗЯ (ну насколько смог понять ) а это часто нужно . Играф без проблем рисует.

* [JGraphT](https://github.com/jgrapht/jgrapht)<br>

            JGraphT is a free Java class library that provides mathematical graph-theory objects and algorithms. 
            It runs on Java 2 Platform (requires JDK 11 or later starting with JGraphT 1.5.0).

* [Chapter 6 : Data Visualization   ipython-books/cookbook-2nd/tree/master/chapter06_viz](https://github.com/ipython-books/cookbook-2nd/tree/master/chapter06_viz)<br>




## GUIs
* [2020: Medium: Create-quick-and-powerful-guis](https://medium.com/datadriveninvestor/create-quick-and-powerful-guis-using-dear-pygui-in-python-713cc138bf5a)<br>
* [github.com/chriskiehl/GooeyExamples](https://github.com/chriskiehl/GooeyExamples)<br>
* [how-to-use-the-easiest-gui](https://codeburst.io/how-to-use-the-easiest-gui-of-your-life-in-python-d3762270a2a0)<br>
* []()<br>
* []()<br>

# [Kalman_filter.md](https://github.com/ftk1000/pyviz/blob/master/Kalman_filter.md)<br>
# [3D_surface.md](https://github.com/ftk1000/pyviz/blob/master/3D_surface.md)<br>

# pyviz - python visualization tricks
[Visualization with Matplotlib on COLAB: github/jakevdp/PythonDataScienceHandbook](https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.00-Introduction-To-Matplotlib.ipynb#scrollTo=TZGGO5cuCvXL)<br>
<br>
[2019: HABR: Другой GitHub: репозитории по Data Science, визуализации данных и глубокому обучению](https://habr.com/ru/company/mailru/blog/437940/)<br>
[2019: HABR: группировки и визуализации данных в Python](https://habr.com/ru/company/mailru/blog/445834/)<br>
[2018: Визуализация данных для вашего Web-проекта](https://habr.com/ru/company/dataart/blog/417947/)<br>
[2017:YT: How to Make a Google Map from Excel ](https://www.youtube.com/watch?v=SLMzhOoA29M)<br>
* [test map](https://www.google.com/maps/d/viewer?hl=en&hl=en&mid=1kTnSD7UGKOotraN42TbkA_1BtefO5o-D&ll=33.078236123943924%2C-96.7541246033679&z=18)<br>

      # (LONG, LAT) = (X,Y) = ( -96.7563	, 33.079976	)
      # https://www.google.com/maps/@33.079976,-96.7563,11z
      
[]()<br>
[]()<br>
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
