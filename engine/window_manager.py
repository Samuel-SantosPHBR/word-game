import pygame

class WindowManager:
    def __init__(self):
        pygame.init()
        self.name_game = 'Word Game'
        self.resolutions = [(800, 600), (1280, 720), (1920, 1080)]
        self.current_res = 1
        self.fullscreen = False
        self.fps_options = [30, 60, 120, 144, 240]
        self.current_fps = 1
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
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
        self.current_res =  max(0, min(self.current_res + direction, len(self.resolutions) - 1))
        self.create_window()

    def change_fps(self, direction):
        self.current_fps = max(0, min(self.current_fps + direction, len(self.fps_options) - 1))

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
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

            self.screen.fill((30, 30, 30))

            fps_text = self.font.render(f"FPS: {self.fps_options[self.current_fps]}", True, (255, 255, 255))
            self.screen.blit(fps_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(self.fps_options[self.current_fps])

        pygame.quit()

if __name__ == "__main__":
    WindowManager().run()
