import pygame
import sys
import random

pygame.init()

# Warna
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Icon Environment
ICON_PLAYER = "🐒"
ICON_NPC = "👻"
ICON_BANANA = "🍌"
ICON_WALL = "🧱"
ICON_DOOR_LOCKED = "🔒"
ICON_DOOR_OPEN = "🚪"

# Font Global
font_score = pygame.font.SysFont('arial', 18)
font_icon = None 

# Global Variables
screen = None
MAP_DATA = []
MAP_WIDTH = 0
MAP_HEIGHT = 0
tile_size = 30
screen_width = 0
screen_height = 0

# Entity
player_grid_x = 0
player_grid_y = 0
npcs = [] 

# Status
total_bananas = 0
score = 0
game_won = False
game_over = False

def generate_maze_layout(rows, cols):
    layout = [['1' for _ in range(cols)] for _ in range(rows)]
    start_x, start_y = cols // 2, rows // 2
    miner_x, miner_y = start_x, start_y
    layout[miner_y][miner_x] = '0'
    area = rows * cols
    steps = int(area * 4.0) 
    
    for _ in range(steps):
        direction = random.randint(0, 3)
        nx, ny = miner_x, miner_y
        if direction == 0: ny -= 1
        elif direction == 1: ny += 1
        elif direction == 2: nx -= 1
        elif direction == 3: nx += 1   
        if 1 <= nx < cols - 1 and 1 <= ny < rows - 1:
            miner_x, miner_y = nx, ny
            layout[miner_y][miner_x] = '0'
    return layout

def draw_emoji(surface, text, grid_x, grid_y, color=(255, 255, 255)):
    text_surf = font_icon.render(text, True, color)
    pixel_x = grid_x * tile_size
    pixel_y = grid_y * tile_size
    text_rect = text_surf.get_rect(center=(pixel_x + tile_size//2, pixel_y + tile_size//2))
    surface.blit(text_surf, text_rect)

def render_game_content(target_surface):
    target_surface.fill(BLACK)
    
    # Gambar Map
    for r in range(MAP_HEIGHT):
        for c in range(MAP_WIDTH):
            char = MAP_DATA[r][c]
            if char == '1': 
                draw_emoji(target_surface, ICON_WALL, c, r, (100, 100, 100))
            elif char == '2': 
                draw_emoji(target_surface, ICON_BANANA, c, r, (255, 255, 0))
            elif char == '3': 
                if score == total_bananas:
                    draw_emoji(target_surface, ICON_DOOR_OPEN, c, r, (0, 255, 0))
                else:
                    draw_emoji(target_surface, ICON_DOOR_LOCKED, c, r, (255, 0, 0))
            elif char == '0': 
                 pygame.draw.circle(target_surface, (40, 40, 40), (c * tile_size + tile_size//2, r * tile_size + tile_size//2), 2)

    # Gambar Player
    draw_emoji(target_surface, ICON_PLAYER, player_grid_x, player_grid_y)
    
    # Gambar NPCs
    for npc in npcs:
        draw_emoji(target_surface, ICON_NPC, npc[1], npc[0])

def play_zoom_animation():
    full_map_surface = pygame.Surface((screen_width, screen_height))
    render_game_content(full_map_surface)
    
    clock = pygame.time.Clock()
    
    start_zoom = 0.15 
    current_zoom = start_zoom
    zoom_speed = 0.015 
    
    player_pixel_x = player_grid_x * tile_size + tile_size // 2
    player_pixel_y = player_grid_y * tile_size + tile_size // 2
    
    animating = True
    while animating:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                animating = False 
        
        current_zoom += zoom_speed
        if current_zoom >= 1.0:
            current_zoom = 1.0
            animating = False 
            
        # Camera
        view_w = screen_width * current_zoom
        view_h = screen_height * current_zoom

        view_x = player_pixel_x - (view_w / 2)
        view_y = player_pixel_y - (view_h / 2)

        if view_x < 0: view_x = 0
        if view_y < 0: view_y = 0
        if view_x + view_w > screen_width: view_x = screen_width - view_w
        if view_y + view_h > screen_height: view_y = screen_height - view_h
        
        camera_rect = pygame.Rect(int(view_x), int(view_y), int(view_w), int(view_h))
        sub_surface = full_map_surface.subsurface(camera_rect)
        
        scaled_surface = pygame.transform.smoothscale(sub_surface, (screen_width, screen_height))
        
        screen.blit(scaled_surface, (0, 0))

        if current_zoom < 0.9:
            skip_text = font_score.render("Press any key to skip", True, WHITE)
            screen.blit(skip_text, (10, 10))
            
        pygame.display.flip()
        clock.tick(60)

def reset_game():
    global MAP_DATA, MAP_WIDTH, MAP_HEIGHT, tile_size, screen, screen_width, screen_height
    global player_grid_x, player_grid_y, npcs, font_icon
    global total_bananas, score, game_won, game_over
    
    score = 0; game_won = False; game_over = False; total_bananas = 0
    npcs = [] 
    
    MAP_WIDTH = random.randint(25, 45)
    max_height = max(15, MAP_WIDTH - 3)
    MAP_HEIGHT = random.randint(15, max_height)
    
    if MAP_WIDTH > 35 or MAP_HEIGHT > 25:
        tile_size = 25 
    else:
        tile_size = 35
    
    try:
        font_icon = pygame.font.SysFont("segoe ui emoji", int(tile_size * 0.8))
    except:
        font_icon = pygame.font.SysFont("arial", int(tile_size * 0.8))

    screen_width = MAP_WIDTH * tile_size
    screen_height = MAP_HEIGHT * tile_size + 50
    
    if screen_height > screen_width:
        MAP_HEIGHT = MAP_WIDTH - 4
        screen_height = MAP_HEIGHT * tile_size + 50

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("ColBan: Zoom Intro Edition 🎥")
    
    MAP_DATA = generate_maze_layout(MAP_HEIGHT, MAP_WIDTH)
    
    available_spots = []
    for r in range(MAP_HEIGHT):
        for c in range(MAP_WIDTH):
            if MAP_DATA[r][c] == '0':
                available_spots.append((r, c))
    
    if len(available_spots) / (MAP_WIDTH * MAP_HEIGHT) < 0.25 or len(available_spots) < 15:
        reset_game()
        return

    p_pos = random.choice(available_spots)
    available_spots.remove(p_pos)
    player_grid_y, player_grid_x = p_pos
    
    jumlah_npc = max(1, len(available_spots) // 40)
    jumlah_npc = min(jumlah_npc, 12) 
    
    safe_spots = []
    min_dist = 8
    for (r, c) in available_spots:
        dist = abs(r - player_grid_y) + abs(c - player_grid_x)
        if dist >= min_dist:
            safe_spots.append((r, c))
    
    for i in range(jumlah_npc):
        if safe_spots:
            pos = random.choice(safe_spots)
            safe_spots.remove(pos)
            if pos in available_spots: available_spots.remove(pos) 
            npcs.append(list(pos))
        else:
            if available_spots:
                pos = random.choice(available_spots)
                available_spots.remove(pos)
                npcs.append(list(pos))

    if available_spots:
        door_pos = random.choice(available_spots)
        available_spots.remove(door_pos)
        MAP_DATA[door_pos[0]][door_pos[1]] = '3'
    
    jumlah_pisang = max(3, int(len(available_spots) * 0.1))
    if len(available_spots) >= jumlah_pisang:
        banana_spots = random.sample(available_spots, jumlah_pisang)
        for (r, c) in banana_spots:
            MAP_DATA[r][c] = '2'
            total_bananas += 1
            
    print(f"Game Ready. Playing Intro Animation...")
    
    play_zoom_animation()

reset_game()

def main():
    global player_grid_x, player_grid_y, npcs, score, game_won, game_over
    clock = pygame.time.Clock()
    running = True
    NPC_MOVE_DELAY = 15; npc_timer = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: reset_game()
                elif not game_won and not game_over:
                    new_x, new_y = player_grid_x, player_grid_y
                    if event.key in [pygame.K_LEFT, pygame.K_a]: new_x -= 1
                    elif event.key in [pygame.K_RIGHT, pygame.K_d]: new_x += 1
                    elif event.key in [pygame.K_UP, pygame.K_w]: new_y -= 1
                    elif event.key in [pygame.K_DOWN, pygame.K_s]: new_y += 1
                    
                    if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
                        target = MAP_DATA[new_y][new_x]
                        if target != '1': 
                            if target == '3': 
                                if score == total_bananas:
                                    game_won = True
                                    player_grid_x, player_grid_y = new_x, new_y
                            else:
                                player_grid_x, player_grid_y = new_x, new_y
                                if target == '2': 
                                    score += 1
                                    MAP_DATA[new_y][new_x] = '0'

        if not game_won and not game_over:
            npc_timer += 1
            if npc_timer >= NPC_MOVE_DELAY:
                npc_timer = 0
                for npc in npcs:
                    npc_r, npc_c = npc[0], npc[1]
                    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                    random.shuffle(dirs)
                    for dr, dc in dirs:
                        nr, nc = npc_r + dr, npc_c + dc
                        if 0 <= nc < MAP_WIDTH and 0 <= nr < MAP_HEIGHT:
                            if MAP_DATA[nr][nc] != '1':
                                npc[0], npc[1] = nr, nc 
                                break 
            for npc in npcs:
                if player_grid_y == npc[0] and player_grid_x == npc[1]: game_over = True

        render_game_content(screen)
        
        if game_won: status = "VICTORY! Press R"
        elif game_over: status = "GAME OVER! Press R"
        else: status = f"{ICON_BANANA}: {score}/{total_bananas} | {ICON_NPC}: {len(npcs)}"
        
        color = GREEN if game_won else (RED if game_over else WHITE)

        pygame.draw.rect(screen, BLACK, (0, screen_height - 40, screen_width, 40))
        screen.blit(font_score.render(status, True, color), (10, screen_height - 35))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit(); sys.exit()

if __name__ == "__main__":
    main()