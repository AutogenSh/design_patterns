'''
适配器模式
作为两个不兼容的接口之间的桥梁。

主要解决：主要解决在软件系统中，常常要将一些"现存的对象"放到新的环境中，而新环境要求的接口是现对象不能满足的。

何时使用： 1、系统需要使用现有的类，而此类的接口不符合系统的需要。
2、想要建立一个可以重复使用的类，用于与一些彼此之间没有太大关联的一些类，包括一些可能在将来引进的类一起工作，这些源类不一定有一致的接口。
3、通过接口转换，将一个类插入另一个类系中。
（比如老虎和飞禽，现在多了一个飞虎，在不增加实体的需求下，增加一个适配器，在里面包容一个虎对象，实现飞的接口。）
'''


class MediaPlayer:
    def play(self, audiotype, filename):
        pass


class AdvancedMediaPlayer(MediaPlayer):
    def playVlc(self, filename):
        pass

    def playMp4(self, filename):
        pass


class VlcPlayer(AdvancedMediaPlayer):
    def playVlc(self, filename):
        print("Playing vlc file. Name:" + filename)

    def playMp4(self, filename):
        pass


class Mp4Player(AdvancedMediaPlayer):
    def playVlc(self, filename):
        pass

    def playMp4(self, filename):
        print("Playing mp4 file. Name:" + filename)


class MediaAdapter(MediaPlayer):
    def __init__(self, audiotype: str):
        if audiotype.lower() == 'vlc':
            self.__player = VlcPlayer()
        elif audiotype.lower() == 'mp4':
            self.__player = Mp4Player()
        else:
            raise NotImplementedError('不支持的类型: %s' % audiotype)

    def play(self, audiotype, filename):
        if audiotype.lower() == 'vlc':
            self.__player.playVlc(filename)
        elif audiotype.lower() == 'mp4':
            self.__player.playVlc(filename)
        else:
            raise NotImplementedError('不支持的类型: %s' % audiotype)


class AudioPlayer(MediaPlayer):
    def play(self, audiotype, filename):
        if audiotype.lower() == 'mp3':
            print("Playing mp3 file. Name:" + filename)
        elif audiotype.lower() == 'vlc' or audiotype.lower() == 'mp4':
            MediaAdapter(audiotype).play(audiotype, filename)
        else:
            print('不支持的类型: %s' % audiotype)


if __name__ == '__main__':
    player = AudioPlayer()
    player.play("mp3", "beyond the horizon.mp3")
    player.play("mp4", "alone.mp4")
    player.play("vlc", "far far away.vlc")
    player.play("avi", "mind me.avi")
