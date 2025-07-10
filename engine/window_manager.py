import pygame

class WindowManager:
    def __init__(self, input_manager):
        pygame.init()
        self.input_manager = input_manager
        self.name_game = 'Word Game'
        self.resolutions = [(800, 600), (1280, 720), (1920, 1080)]
        self.current_res = 1
        self.fullscreen = False
        self.fps_options = [30, 60, 120, 144, 240]
        self.current_fps = 1
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.images = []
        self.create_window()

    def create_window(self):
        flags = self.get_flags_window()
        self.set_flags_screen(flags)
        self.change_caption()

    def get_flags_window(self):
        return pygame.FULLSCREEN if self.fullscreen else pygame.RESIZABLE

    def set_flags_screen(self, flags):
        self.screen = pygame.display.set_mode(self.resolutions[self.current_res], flags)

    def change_caption(self):
        pygame.display.set_caption(self.name_game)

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.create_window()

    def change_resolution(self, direction):
        self.current_res = max(0, min(self.current_res + direction, len(self.resolutions) - 1))
        self.create_window()

    def change_fps(self, direction):
        self.current_fps = max(0, min(self.current_fps + direction, len(self.fps_options) - 1))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_F7:
                    self.change_fps(-1)
                elif event.key == pygame.K_F8:
                    self.change_fps(1)
                elif event.key == pygame.K_F9:
                    self.change_resolution(-1)
                elif event.key == pygame.K_F10:
                    self.change_resolution(1)
                elif event.key == pygame.K_F11:
                    self.toggle_fullscreen()
        return True


    def render(self, images_data):
        self.screen.fill((30, 30, 30))
        fps_index = max(0, min(self.current_fps, len(self.fps_options) - 1))
        fps_text = self.font.render(f"FPS: {self.fps_options[fps_index]}", True, (255, 255, 255))
        self.screen.blit(fps_text, (10, 10))
        for image_data in images_data:
            print(image_data['path'], image_data['x'], image_data['y'])
            img = pygame.image.load(image_data['path'])
            img = pygame.transform.scale(img, (50, 50))
            self.screen.blit(img, (image_data['x'], image_data['y']))
        pygame.display.flip()
        self.clock.tick(self.fps_options[fps_index])