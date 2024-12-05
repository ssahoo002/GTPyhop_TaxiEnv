(define (problem taxi-problem)
    (:domain taxi)
    (:objects
        taxi1 - taxi
        passenger1 passenger2 passenger3 - passenger
        loc11 loc12 loc13 loc14 loc15 loc16 loc17 loc18 loc19 loc20 - location
        loc21 loc22 loc23 loc24 loc25 loc26 loc27 loc28 loc29 loc30 - location
        loc31 loc32 loc33 loc34 loc35 loc36 loc37 loc38 loc39 loc40 - location
        loc41 loc42 loc43 loc44 loc45 loc46 loc47 loc48 loc49 loc50 - location
        loc51 loc52 loc53 loc54 loc55 loc56 loc57 loc58 loc59 loc60 - location
        loc61 loc62 loc63 loc64 loc65 loc66 loc67 loc68 loc69 loc70 - location
        loc71 loc72 loc73 loc74 loc75 loc76 loc77 loc78 loc79 loc80 - location
        loc81 loc82 loc83 loc84 loc85 loc86 loc87 loc88 loc89 loc90 - location
        loc91 loc92 loc93 loc94 loc95 loc96 loc97 loc98 loc99 loc100 - location
        bush1 bush2 bush3 bush4 bush5 bush6 bush7 bush8 bush9 bush10 - bush
    )

    (:init
        (at taxi1 loc11)
        (at passenger1 loc12)
        (at passenger2 loc13)
        (at passenger3 loc14)
        (at passenger4 loc15)
        (at passenger5 loc16)

        (bush-at bush1 loc15)
        (bush-at bush2 loc25)
        (bush-at bush3 loc35)
        (bush-at bush4 loc45)
        (bush-at bush5 loc55)
        (bush-at bush6 loc55)
        (bush-at bush7 loc55)
        (bush-at bush8 loc55)
        (bush-at bush9 loc55)
        (bush-at bush10 loc55)

        (move-space loc11)
        (move-space loc12)
        (move-space loc13)
        (move-space loc14)
        (move-space loc16)
        (move-space loc17)
    )
    (:goal
    (and
        (at passenger1 loc100)               ; Example goal: Drop passenger 1 at (10, 10) or loc100
        (at passenger2 loc100)               ; Drop passenger 2 at (10, 10)
        (at passenger3 loc100)               ; Drop passenger 3 at (10, 10)
    )
    )
)