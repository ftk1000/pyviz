[]()<br>
[MATPLOTLIB ANIMATION:  https://matplotlib.org/3.1.1/api/animation_api.html](https://matplotlib.org/3.1.1/api/animation_api.html)<br>
[YT 2015: How to use FFMPEG](https://www.youtube.com/watch?v=MPV7JXTWPWI)<br>
[STACKOVERFLOW: Suggestions on how to install ffmpeg](https://stackoverflow.com/questions/13316397/matplotlib-animation-no-moviewriters-available)<br>
[WIKIHOW: How to Install FFmpeg on Windows](https://www.wikihow.com/Install-FFmpeg-on-Windows)<br>


[YT 2019: Animations With matplotlib](https://www.youtube.com/watch?v=GtZxk8Wa3Jw)<br>




# demo1: SIN curve

    %matplotlib inline
    ################################################################
    # code from https://www.youtube.com/watch?v=GtZxk8Wa3Jw
    ################################################################
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from IPython import display

    output = plt.plot([])
    plt.close()
    print('output of plt.plot() is object = ', output[0])

    x = np.linspace(0, 2*np.pi, 100)
    fig = plt.figure()

    line, = plt.plot([])
    # print(line)

    # OTHER SETUP
    plt.xlim(0, 2*np.pi)
    plt.ylim(-1,1)

    def animate(frame):
        # update plot
        y = np.sin(x +2*np.pi * frame/100)
        line.set_data((x,y))

    anim = FuncAnimation( fig, animate, frames=100, interval=20 )    
    video = anim.to_html5_video()
    html = display.HTML(video)
    display.display(html)
    plt.close()
    
    
# demo2: a Dot MOVING ON ELLIPTIC TRAJECTORY

    %matplotlib inline
    ################################################################
    # code from https://www.youtube.com/watch?v=GtZxk8Wa3Jw
    ################################################################
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from IPython import display

    output = plt.plot([])
    plt.close()
    print('output of plt.plot() is object = ', output[0])

    x = np.linspace(0, 2*np.pi, 100)
    fig = plt.figure()

    lines = plt.plot([], 'o', c='r')
    line = lines[0]
    # line, = plt.plot([])
    print( 'line = ', line)

    # OTHER SETUP
    plt.axis('scaled')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    def animate(frame):
        # update plot
        x = 1.3*np.cos(frame/100*2*np.pi)
        y = 0.6*np.sin(frame/100*2*np.pi)
        line.set_data((x,y))

    anim = FuncAnimation( fig, animate, frames=100, interval=30 )    
    video = anim.to_html5_video()
    html = display.HTML(video)
    display.display(html)
    plt.close()    
    
    
    
# demo3 : simple LINE animation

    %matplotlib notebook
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    x_data = []
    y_data = []

    fig, ax = plt.subplots()
    ax.set_xlim(0, 105)
    ax.set_ylim(0, 12)
    line, = ax.plot(0, 0)

    def animation_frame(i):
        x_data.append(i * 10)
        y_data.append(i)

        line.set_xdata(x_data)
        line.set_ydata(y_data)
        return line, 

    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 10, 0.1), interval=10)
    plt.show()

# How to enable animation on Win10 with Anaconda?

* read [https://stackoverflow.com/questions/13316397/matplotlib-animation-no-moviewriters-available](https://stackoverflow.com/questions/13316397/matplotlib-animation-no-moviewriters-available)<br>
* open Anaconda CMD line window<br>
* Install ffmpeg by running the following command
    >> conda install -c conda-forge ffmpeg
* re-launch **jupyter notebook**
    
