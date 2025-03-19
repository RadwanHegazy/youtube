
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.resize import resize
import os



class ResolutionParser :
    __results = []
    __resolutions = [
        (1280, 720),  # 720p
        (854, 480),   # 480p
        (640, 360),   # 360p
        (426, 240),   # 240p
    ]
    __duration = ""

    def __init__(self, video_path):
        self.video_path = video_path

    def get_duration(self) : 
        return self.__duration
    
    def get_video_resolution(self):
        """Get the original resolution of the video."""
        clip = VideoFileClip(self.video_path)
        self.__duration = clip.duration
        width, height = clip.size
        clip.close()
        return width, height

    def resize_video(self, output_path, new_width, new_height):
        """Resize the video to the specified resolution and save it."""
        clip = VideoFileClip(self.video_path)
        resized_clip = resize(clip, width=new_width, height=new_height)
        resized_clip.write_videofile(output_path, codec="libx264")  # Save the resized video
        clip.close()
        resized_clip.close()

    def create_multiple_resolutions(self, output_folder):
        """
        Create multiple resized versions of the video.
        :param video_path: Path to the original video file.
        :param resolutions: List of tuples containing (width, height) for each resolution.
        """

        if not os.path.exists(output_folder) : 
            os.mkdir(output_folder)

        original_width, original_height = self.get_video_resolution()

        for i, (width, height) in enumerate(self.__resolutions):
            if width > original_width or height > original_height:
                print(f"Skipping {width}x{height} because it's larger than the original resolution.")
                continue
            
            
            output_path = f"{output_folder}/resized_video_{i+1}_{width}x{height}.mp4"
            self.resize_video(output_path, width, height)
            self.__results.append({
                'path' : output_path,
                'quality' : f"{height}p"
            })


    def get_results(self) :
        return self.__results 

# Example usage
# if __name__ == "__main__":
    # video_path = "../test.mp4"
    
    # action = ResolutionParser(video_path)
    # action.create_multiple_resolutions(output_folder='media/video-media/')
    # print(action.get_results())