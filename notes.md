# Turtle Graphics - Breakout
## Design Notes


```mermaid
    %% Rough outline of program
        
    flowchart TB

    classDef orange fill:#a60,color:#000,stroke:#000,stroke-width:3px
    
    S([Start]) --> A
    A(Initialize:\nLives\nLevel\nBall direction\nBall speed) --> A1(Draw screen)
    A1 --> B(While lives remaining)
    B --> B1{Ball hits\nedge of\nscreen}
    B1 --Yes--- B2(Bounce)
    B1 --> C{Ball hits\npaddle}
    C --Yes--- D(Bounce)
    C --> E{Ball hits\nbrick} 
    E -->|Yes| F(Bounce\nDestroy brick)
    E --> J{All bricks\ndestroyed}
    H -.->|No| B
    J -->|No| G{Ball at\nbottom of\nscreen}
    J -->|Yes| K(Increment Level)
    G -->|Yes| H(Lose life\nReset ball and paddle\nTime delay)
    G -.->|No| B
    K -.-> A1
    
    class B1 orange
    class C orange
    class E orange
    class G orange
    class J orange

```

### Ideas:
1. Create background - fancy graphics 
2. Different layouts for levels
3. Design bricks - some bricks with special properties \
&emsp; Multiple hits\
&emsp; Drop bombs \
&emsp; &emsp; Kill player \
&emsp; &emsp; Deduct lives \
&emsp; &emsp; Deduct points \
&emsp; &emsp; Make paddle smaller for a time \
&emsp; &emsp; Fast ball for a time \
&emsp; Drop bonuses \
&emsp; &emsp; Extra points \
&emsp; &emsp; Extra lives \
&emsp; &emsp; Add gun to paddle for a time \
&emsp; &emsp; Ball can punch through bricks for a time \
&emsp; &emsp; Make paddle larger for a time \
&emsp; &emsp; Slow ball for a time \
&emsp; Explosive bricks 
4. Design player paddle - use multiple turtles. 
5. Detect ball collision with paddle \
&emsp; Angle of bounce depends upon which turtle is contacted 
6. Detect ball collision with brick \
&emsp; Angle of bounce depends upon which side of the brick is hit, \
&emsp; and direction of ball travel 
7. Create Algorithm to auto-generate brick patterns