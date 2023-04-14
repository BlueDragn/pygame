import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the canvas
canvas_width = 600
canvas_height = 600
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Sprite Animation")

# Load the player image
player_image = pygame.image.load("assets/sprite animation techniques/shadow_dog.png")

# Set up the animation variables
sprite_width = 575
sprite_height = 523
frame_x = 0
frame_y = 0
game_frame = 0
stagger_frames = 5

# Start the animation loop
while True:
    # Clear the canvas with white color
    canvas.fill((255, 255, 255))

    # Calculate the current position in the sprite sheet
    position = (game_frame // stagger_frames) % 6
    frame_x = sprite_width * position

    # Draw the current frame of the animation
    # The draw function takes the image, the position where it should be drawn and the area of the image to be drawn
    canvas.blit(player_image, (0, 0), (frame_x, frame_y * sprite_height, sprite_width, sprite_height))

    # Update the game frame
    game_frame += 1

    # Update the canvas
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the close button is pressed, quit Pygame and exit the program
            pygame.quit()
            quit()

    # Delay for a short time to allow the canvas to be displayed
    time.sleep(0.01)
cle