from manim import *
from this import d, s

class ZenOfPython(Scene):
    def construct(self):
        string = "".join([d.get(c, c) for c in s]).replace('\n\n', '\n').strip()
        line_lst = string.strip().split('\n')
        text_lst = [Text(line, font_size=36) for line in line_lst]
        footer = Text('Created by szchixy, Powered by manimgl', font_size=20)
        self.play(Write(text_lst[0]))
        self.wait()
        self.play(FadeOut(text_lst[0]))
        self.wait()
        self.play(FadeIn(text_lst[1]))
        for i in range(1, len(text_lst)-1):
            self.wait(0.5)
            self.play(FadeOut(text_lst[i], shift=UP), FadeIn(text_lst[i+1], shift=UP))
        self.play(FadeIn(footer), footer.animate.shift(DOWN))
        self.wait()

if __name__ == '__main__':
    ZenOfPython().render()
