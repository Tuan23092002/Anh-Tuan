import ffmpeg

input_video_path = "/home/anhtuanuser/Documents/make_video/static/final_output.mp4"
output_video_path = "/home/anhtuanuser/Documents/make_video/static/output_video_1080p_nhatban.mp4"

# Sử dụng ffmpeg để chuyển đổi video
(
    ffmpeg.input(input_video_path)
    .output(output_video_path, vf='scale=1920:1080', acodec='copy')
    .run()
)

print("Video đã được chuyển đổi thành 1080p và lưu tại:", output_video_path)
