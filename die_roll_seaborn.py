from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys

def update(frame_number, rolls, faces, frequencies):
    for i in range(rolls):
        frequencies[random.randrange(1,7) - 1] += 1

    plt.cla()
    axes = sns.barplot(faces,frequencies,palette='bright')
    axes.set_title(f"Die frequencies for {sum(frequencies):,} rolls")
    axes.set(xlabel="die value", ylabel="frequency")
    axes.set_ylim(top=max(frequencies) * 1.18)

    for bar, frequency in zip(axes.patches,frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')



number_of_frames = 100
rolls_per_frame = 68

plt.show()

sns.set_style('whitegrid')
figure = plt.figure("rolling")
values = list(range(1,7))
frequencies = [0] * 6

die_animation = animation.FuncAnimation(figure, update, repeat=False, frames=number_of_frames, interval=33, fargs=(rolls_per_frame, values, frequencies))

plt.show()