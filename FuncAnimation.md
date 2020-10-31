[]()<br>
[]()<br>
[]()<br>
[YT 2015: How to use FFMPEG](https://www.youtube.com/watch?v=MPV7JXTWPWI)<br>
[STACKOVERFLOW: Suggestions on how to install ffmpeg](https://stackoverflow.com/questions/13316397/matplotlib-animation-no-moviewriters-available)<br>
[A basic example how to create animation | Matplotlib Tutorial](https://learndataanalysis.org/a-basic-example-how-to-create-animation-atplotlib-tutorial/)<br>


[YT 2019: Animations With matplotlib](https://www.youtube.com/watch?v=GtZxk8Wa3Jw)<br>

# FuncAnimation_demo.ipynb

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from IPython import display

    output = plt.plot([])
    plt.close()
    print(output[0])

    x = np.linspace(0, 2*np.pi, 100)
    fig = plt.figure()

    line, = plt.plot([])
    print(line)

    # OTHER SETUP
    plt.xlim(0, 2*np.pi)
    plt.ylim(-1,1)

    def animate(frame):
        # update plot
        y = npsin(x +2*np.pi * frame/100)
        line.set_data((x,y))

    anim = FuncAnimation( fig, animate, frames=100, interval=20 )    
    video = anim.to_html5_video()
    html = display.HTML(video)
    display.display(html)
    plt.close()
    
    
