"""
Pygame web-compatible game implementation.
This file contains the main game logic designed to work with pygame-web/pygbag.
"""

import pygame
import asyncio
import math
import random
import sys

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

class Ball:
    """A simple ball object that bounces around the screen."""
    
    def __init__(self, x, y, radius=20):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel_x = random.uniform(-5, 5)
        self.vel_y = random.uniform(-5, 5)
        self.color = random.choice([RED, GREEN, BLUE, YELLOW, PURPLE])
        
    def update(self):
        """Update ball position and handle collision with screen edges."""
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Bounce off edges
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.vel_x = -self.vel_x
            self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
            
        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
            self.vel_y = -self.vel_y
            self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))
    
    def draw(self, screen):
        """Draw the ball on the screen."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius, 2)

class Game:
    """Main game class handling game state and logic."""
    
    def __init__(self):
        self.screen = None
        self.clock = None
        self.running = True
        self.balls = []
        self.font = None
        self.score = 0
        self.mouse_pos = (0, 0)
        
    def initialize(self):
        """Initialize pygame and game components."""
        try:
            pygame.init()
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Pygame Web Demo - Bouncing Balls")
            self.clock = pygame.time.Clock()
            
            # Initialize font for text rendering
            self.font = pygame.font.Font(None, 36)
            
            # Create initial balls
            for _ in range(3):
                ball = Ball(
                    random.randint(50, SCREEN_WIDTH - 50),
                    random.randint(50, SCREEN_HEIGHT - 50)
                )
                self.balls.append(ball)
                
            print("Game initialized successfully!")
            return True
            
        except Exception as e:
            print(f"Error initializing game: {e}")
            return False
    
    def handle_events(self):
        """Handle pygame events including user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Add a new ball at random position
                    ball = Ball(
                        random.randint(50, SCREEN_WIDTH - 50),
                        random.randint(50, SCREEN_HEIGHT - 50)
                    )
                    self.balls.append(ball)
                    self.score += 10
                elif event.key == pygame.K_r:
                    # Reset game
                    self.balls.clear()
                    self.score = 0
                    for _ in range(3):
                        ball = Ball(
                            random.randint(50, SCREEN_WIDTH - 50),
                            random.randint(50, SCREEN_HEIGHT - 50)
                        )
                        self.balls.append(ball)
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Add ball at mouse position
                    ball = Ball(event.pos[0], event.pos[1])
                    self.balls.append(ball)
                    self.score += 5
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
    
    def update(self):
        """Update game state."""
        # Update all balls
        for ball in self.balls:
            ball.update()
        
        # Remove balls if too many (keep performance reasonable)
        if len(self.balls) > 20:
            self.balls.pop(0)
    
    def draw(self):
        """Draw all game elements."""
        # Clear screen
        self.screen.fill(BLACK)
        
        # Draw all balls
        for ball in self.balls:
            ball.draw(self.screen)
        
        # Draw UI text
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        balls_text = self.font.render(f"Balls: {len(self.balls)}", True, WHITE)
        self.screen.blit(balls_text, (10, 50))
        
        # Draw instructions
        instructions = [
            "SPACE: Add random ball (+10 pts)",
            "Click: Add ball at cursor (+5 pts)",
            "R: Reset game",
            "ESC: Exit"
        ]
        
        for i, instruction in enumerate(instructions):
            text = pygame.font.Font(None, 24).render(instruction, True, WHITE)
            self.screen.blit(text, (10, SCREEN_HEIGHT - 100 + i * 20))
        
        # Draw mouse position
        mouse_text = pygame.font.Font(None, 24).render(
            f"Mouse: {self.mouse_pos[0]}, {self.mouse_pos[1]}", True, WHITE
        )
        self.screen.blit(mouse_text, (SCREEN_WIDTH - 200, 10))
        
        # Update display
        pygame.display.flip()

async def main():
    """Main game loop with async support for web deployment."""
    game = Game()
    
    # Initialize the game
    if not game.initialize():
        print("Failed to initialize game!")
        return
    
    print("Game loop starting...")
    print("Controls:")
    print("- SPACE: Add random ball")
    print("- Click: Add ball at mouse position")
    print("- R: Reset game")
    print("- ESC: Exit")
    
    # Main game loop
    while game.running:
        try:
            # Handle events
            game.handle_events()
            
            # Update game state
            game.update()
            
            # Draw everything
            game.draw()
            
            # Control frame rate
            game.clock.tick(FPS)
            
            # Essential for web deployment - yield control to browser
            await asyncio.sleep(0)
            
        except Exception as e:
            print(f"Error in game loop: {e}")
            break
    
    print("Game loop ended.")
    pygame.quit()

if __name__ == "__main__":
    # Run the game
    asyncio.run(main())
