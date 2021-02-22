TARGET = f
CFLAGS = -Wall

OBJS := $(patsubst %.c,%.o,$(wildcard *.c))
CC = gcc
OPTION = -O3

$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS) $(OPTION) -lm 

%.o: %.cc $(HEADER)
	$(CC) $(CFLAGS) -c $<

clean:
	rm -rf *.o
