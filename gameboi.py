import sys
import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Setup Display & Dimensions
WIDTH, HEIGHT = 900, 700
TOOLBAR_HEIGHT = 80
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint Studio")

# 3. Colors Definition
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
LIGHT_GRAY = (240, 240, 240)

# Brush Colors
PALETTE = [
    (0, 0, 0),        # Black
    (255, 0, 0),      # Red
    (0, 200, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 128, 0),    # Orange
    (128, 0, 128),    # Purple
    (0, 255, 255),    # Cyan
]

# 4. Canvas Surface Setup
canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

# 5. Drawing State Variables
drawing = False
current_color = PALETTE[0]
brush_size = 5
tool = "BRUSH"  # Options: "BRUSH", "ERASER"
last_pos = None

# Font Setup
font = pygame.font.SysFont("Arial", 16, bold=True)


def draw_toolbar():
    """Renders the top toolbar interface with color swatches and tool buttons."""
    # Background bar
    pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    pygame.draw.line(screen, DARK_GRAY, (0, TOOLBAR_HEIGHT), (WIDTH, TOOLBAR_HEIGHT), 2)

    # Render Color Palette
    for i, color in enumerate(PALETTE):
        x = 20 + i * 40
        y = 20
        rect = pygame.Rect(x, y, 30, 30)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)  # Border

        # Highlight active color selection
        if tool == "BRUSH" and current_color == color:
            pygame.draw.rect(screen, (50, 150, 250), rect.inflate(6, 6), 3)

    # Render Eraser Button
    eraser_rect = pygame.Rect(360, 20, 80, 40)
    eraser_bg = GRAY if tool == "ERASER" else LIGHT_GRAY
    pygame.draw.rect(screen, eraser_bg, eraser_rect)
    pygame.draw.rect(screen, BLACK, eraser_rect, 2)
    eraser_text = font.render("ERASER", True, BLACK)
    screen.blit(eraser_text, (eraser_rect.x + 8, eraser_rect.y + 12))

    # Render Clear Button
    clear_rect = pygame.Rect(455, 20, 80, 40)
    pygame.draw.rect(screen, LIGHT_GRAY, clear_rect)
    pygame.draw.rect(screen, BLACK, clear_rect, 2)
    clear_text = font.render("CLEAR", True, BLACK)
    screen.blit(clear_text, (clear_rect.x + 14, clear_rect.y + 12))

    # Render Brush Size & Indicator
    size_label = font.render(f"Size: {brush_size}px ([ / ])", True, BLACK)
    screen.blit(size_label, (560, 32))

    # Return clickable UI elements for event handling
    return eraser_rect, clear_rect


# Main Application Loop
clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    # Process Events
    for event in pygame.event.type:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard Controls
        if event.type == pygame.KEYDOWN:
            # Increase/decrease brush size using [ and ]
            if event.key == pygame.K_RIGHTBRACKET:
                brush_size = min(brush_size + 2, 50)
            elif event.key == pygame.K_LEFTBRACKET:
                brush_size = max(brush_size - 2, 1)

        # Mouse Pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mx, my = event.pos

                # Toolbar Click Handling
                if my < TOOLBAR_HEIGHT:
                    # Check palette clicks
                    for i, color in enumerate(PALETTE):
                        px = 20 + i * 40
                        if px <= mx <= px + 30 and 20 <= my <= 50:
                            current_color = color
                            tool = "BRUSH"

                    # Check Eraser click
                    eraser_r, clear_r = draw_toolbar()
                    if eraser_r.collidepoint(mx, my):
                        tool = "ERASER"

                    # Check Clear Canvas click
                    if clear_r.collidepoint(mx, my):
                        canvas.fill(WHITE)

                # Canvas Click Handling
                else:
                    drawing = True
                    last_pos = (mx, my - TOOLBAR_HEIGHT)

        # Mouse Released
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None

    # Handle Continuous Drawing
    if drawing:
        mx, my = pygame.mouse.get_pos()
        canvas_y = my - TOOLBAR_HEIGHT

        # Ensure drawing stays within canvas bounds
        if canvas_y >= 0:
            current_pos = (mx, canvas_y)
            draw_color = WHITE if tool == "ERASER" else current_color

            if last_pos:
                # Draw continuous lines to prevent gaps when dragging mouse fast
                pygame.draw.line(canvas, draw_color, last_pos, current_pos, brush_size * 2)
                pygame.draw.circle(canvas, draw_color, current_pos, brush_size)

            last_pos = current_pos

    # Render Canvas & UI to Screen
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))
    draw_toolbar()

    pygame.display.flip()
    clock.tick(120)  # Smooth 120 FPS