
#### How to install skfda
https://pypi.org/project/scikit-fda/

1. goto Anaconda command prompt and run CMD> pip install scikit-fda
2. if you get an error fix it as described below

  error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

#### error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

To fix the error above to go
https://docs.microsoft.com/en-us/answers/questions/136595/error-microsoft-visual-c-140-or-greater-is-require.html

download vs_buildtools__618911391.1599087397.exe and follow the instructions


***

[https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html](https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html)<br>

      An Axes3D object is created just like any other axes using the projection=‘3d’ keyword. 
      
[https://matplotlib.org/3.1.0/gallery/mplot3d/surface3d.html](https://matplotlib.org/3.1.0/gallery/mplot3d/surface3d.html)<br>      






***

# [My notes on KF](https://github.com/ftk1000/pyviz/blob/master/Kalman_filter.md)<br>

***

# Smooth fitting and surface plotting links

[https://github.com/nschloe/smoothfit](https://github.com/nschloe/smoothfit)<br>
[ftk1000/pyviz: 2D extrapolation and Surf Plotting with SKFDA](https://github.com/ftk1000/pyviz/blob/master/3D_skfda_extrapolation_demo2.ipynb)<br>
[ftk1000/pyviz: Smoothing and Forecasting posts from Marco Cerliani](https://github.com/ftk1000/pyviz/blob/master/smoothing_forecasting.md)<br>
[ftk1000/pyviz: 3D_triangulation.ipynb](https://github.com/ftk1000/pyviz/blob/master/3D_triangulation.ipynb)<br>
[MATLAB Smoothing related videos](https://www.mathworks.com/videos/search.html?q=smoothing&page=1)<br>
[MATLAB: signal-smoothing ](https://www.mathworks.com/videos/signal-smoothing-97060.html)<br>
   - moving average filter (con:lag)<br>
   - Savitzky-Golay Filter (3rd , 4th order poly)<br>
   
[MATLAB Curve fitting toolbox](https://www.mathworks.com/videos/curve-fitting-toolbox-overview-61198.html?s_tid=srchtitle)<br>
[MATLAB: data-driven-fitting](https://www.mathworks.com/videos/data-driven-fitting-with-matlab-81809.html)<br>

## github.com/nschloe
[github.com/nschloe](https://github.com/nschloe?tab=repositories)<br>
[nschloe/meshzoo](https://github.com/nschloe/meshzoo)<br>
[nschloe/smoothfit](https://github.com/nschloe/smoothfit)<br>
[]()<br>
[]()<br>

# Lowess

[2019: Mike Langen: Creating powerfull LOWESS graphs in Python](https://medium.com/@langen.mu/creating-powerfull-lowess-graphs-in-python-e0ea7a30b17a)<br>
[www.jtrive.com/loess-nonparametric-scatterplot-smoothing-in-python](http://www.jtrive.com/loess-nonparametric-scatterplot-smoothing-in-python.html#Footnotes:)<br>
[2020: LOWESS from github.com/CCGE-Cambridge/lowess](https://github.com/CCGE-Cambridge/lowess)<br>





G:\My Drive\SHARE\RSRP_modeling_data_v2\CTX_131282\o020_preprocess_single_map

G:\My Drive\__C\Users\khafifa\Documents\ban_3tbls\PPT_slides\Spline based approximation of RSRP.pptx

# PYSPARK CODE

C:\Users\khafifa\Downloads\RSRP_Model_Creation_in_PySpark.docx

PS C:\Users\khafifa> 2020/11/20 12:05:56 [INFO] Starting yubico-agent on \\.\pipe\S-1-5-21-2080630907-2779048583-386258426-468246\openssh-yubico-agent



# ANIMATION

https://github.com/ftk1000/pyviz/blob/master/FuncAnimation.md

https://www.youtube.com/watch?v=GtZxk8Wa3Jw

http://localhost:8888/notebooks/__C/Users/khafifa/PY_CODE/animation_demo.ipynb#code-from-https://www.youtube.com/watch?v=GtZxk8Wa3Jw

https://matplotlib.org/gallery/animation/random_walk.html





# SPLINES 

https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html#id1

https://python-graph-gallery.com/371-surface-plot/

https://machinelearningmastery.com/multivariate-adaptive-regression-splines-mars-in-python/
[Markdown editors](https://www.oberlo.com/blog/markdown-editors)<br>

 - https://remarkableapp.github.io/linux.html   FOR LINUX
 - https://typora.io/#windows
 - https://github.com/michelolvera/vs-ghostwriter


============================================================



ROTATION OF 3D plt_surface works only with 

3d_surface_examples.ipynb

NOTHING                 <- does not work

%matplotlib notebook    <- works

%matplotlib inline      <- does not work



3d_plot_demo

nice use of plt.color(x,y,z)



# Python 3D surfaces and curves

[Mplot3D Tutorial: Wireframe, Surface, Tri-Surface plots etc ](https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html)<br>

An **Axes3D** object is created just like any other axes using the projection=‘3d’ keyword. Create a new matplotlib.figure.Figure and add a new axes to it of type Axes3D:

[SmoothFit (Pikhletski Recommendation): github.com/nschloe/smoothfit](https://github.com/nschloe/smoothfit)<br>

Given experimental data, it is often desirable to produce a function whose values match the data to some degree. This package implements a robust approach to data fitting based on the [REGULARIZED minimization problem](https://eeweb.engineering.nyu.edu/iselesni/lecture_notes/least_squares/least_squares_SP.pdf). Unlike [polynomial regression](https://en.wikipedia.org/wiki/Polynomial_regression) or Gauss-Newton, smoothfit makes no assumptions about the function other than that it is smooth.
		
[2013: Ivan Selesnick: NYU-Poly Lecture Notes: Least Squares with Examples in Signal Processing](https://eeweb.engineering.nyu.edu/iselesni/lecture_notes/least_squares/least_squares_SP.pdf)<br>

These notes address (approximate) solutions to linear equations by least
		squares. We deal with the ‘easy’ case wherein the system matrix is full
		rank. If the system matrix is rank deficient, then other methods are
		needed, e.g., QR decomposition, singular value decomposition, or the
		pseudo-inverse, [Ref:2, Ref:3].
		
In these notes, least squares is illustrated by applying it to several basic
		problems in signal processing: 1. Linear prediction, 2. Smoothing, 3. Deconvolution, 
		4. System identification, 5. Estimating missing data

[Tufte-style plots. Simply select the **dufte** style and, if desired, call **dufte.legend()** to get line annotations on the right.](https://github.com/nschloe/dufte/blob/master/README.md)<br>
[]()<br>
[]()<br>
[]()<br>
[SciPy: Triangulation:  scipy.spatial.Delaunay](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html)<br>


https://towardsdatascience.com/neural-networks-ensemble-33f33bea7df3

https://github.com/cerlymarco/MEDIUM_NoteBook

https://github.com/cerlymarco/tsmoothie

https://github.com/cerlymarco/keras-hypetune

https://towardsdatascience.com/time-series-smoothing-for-better-forecasting-7fbf10428b2





### SciKit-FDA<br>

Before beginning to use the functionalities of the package, it is necessary to represent the data in functional form, using one of the following classes, which allow the visualization, evaluation and treatment of the data in a simple way, using the advantages of the object-oriented programming.

[SciKit-FDA: Extrapolation. Shows the usage of the different types of extrapolation.](https://fda.readthedocs.io/en/latest/auto_examples/plot_extrapolation.html#)<br>

[SciKit-FDA: BSpline (skfda.representation.basis.BSpline)](https://fda.readthedocs.io/en/latest/modules/autosummary/skfda.representation.basis.BSpline.html?highlight=extrapolation#examples-using-skfda-representation-basis-bspline)<br>


### python triangulation 2d






### python triangulation 3d

https://plotly.com/python/v3/surface-triangulation/

https://matplotlib.org/3.1.0/gallery/mplot3d/trisurf3d_2.html

https://matplotlib.org/3.3.3/api/tri_api.html

https://stackoverflow.com/questions/20025784/how-to-visualize-3d-delaunay-triangulation-in-python




### how-does-numpy-newaxis-work-and-when-to-use-it

https://stackoverflow.com/questions/29241056/how-does-numpy-newaxis-work-and-when-to-use-it

Simply put, numpy.newaxis is used to increase the dimension of the existing array by one more dimension, when used once. Thus,

1D array will become 2D array

2D array will become 3D array

4D array will become 5D array







https://stackoverflow.com/questions/20025784/how-to-visualize-3d-delaunay-triangulation-in-python

https://matplotlib.org/3.1.0/gallery/mplot3d/trisurf3d_2.html

https://matplotlib.org/3.3.3/api/tri_api.html

https://stackoverflow.com/questions/45243563/creating-a-triangulation-for-use-in-matplotlibs-plot-trisurf-with-matplotlib-tr


https://plotly.com/python/v3/surface-triangulation/

https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html


# PYTHON LOWESS (Locally Weighted Scatterplot Smoothing)

https://www.statsmodels.org/stable/generated/statsmodels.nonparametric.smoothers_lowess.lowess.html

  - statsmodels.nonparametric.smoothers_lowess.lowess(endog, exog, frac=0.6666666666666666, it=3, delta=0.0, xvals=None, is_sorted=False, missing='drop', return_sorted=True)
  
  -  CODE: https://www.statsmodels.org/stable/_modules/statsmodels/nonparametric/smoothers_lowess.html#lowess



# MATLAB smoothing

https://www.mathworks.com/matlabcentral/fileexchange/69889-forward-backwards-kalman-filter





# MATLAB + PYTHON

https://github.com/arokem/python-matlab-bridge








