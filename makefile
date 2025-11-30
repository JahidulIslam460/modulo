# Makefile for C Modulo Project
CC = gcc
CFLAGS = -Wall -std=c99
TARGET = modulo_app
TEST_TARGET = test_modulo
BUILD_DIR = build

all: build test

build: $(BUILD_DIR)
	@echo "🔨 Building C application..."
	$(CC) $(CFLAGS) -o $(BUILD_DIR)/$(TARGET) modulo.c
	$(CC) $(CFLAGS) -o $(BUILD_DIR)/$(TEST_TARGET) test_modulo.c
	@echo "✅ Build completed successfully!"

$(BUILD_DIR):
	@mkdir -p $(BUILD_DIR)

test: build
	@echo "🧪 Running unit tests..."
	./$(BUILD_DIR)/$(TEST_TARGET)
	@echo "✅ All tests passed!"

clean:
	@echo "🧹 Cleaning build files..."
	rm -rf $(BUILD_DIR)

.PHONY: all build test clean
