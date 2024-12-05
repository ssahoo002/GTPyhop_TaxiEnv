(define (domain taxi)
    (:requirements :strips)
    (:types taxi passenger location)

    (:predicates
        (at ?t - taxi ?l - location)
        (at ?p - passenger ?l - location)
        (has-passenger ?t - taxi ?p - passenger)
        (bush-at ?b - bush ?l - location)
        (move-space ?l - location)
    )

    (:action pick-up
        :parameters (?t - taxi ?p - passenger ?l - location)
        :precondition (and (at ?t ?l) (at ?p ?l))
        :effect (and (not (at ?p ?l) (has-passenger ?t ?p)))
    )

    (:action drop-off
        :parameters (?t - taxi ?p - passenger ?l - location)
        :precondition (and (at ?t ?l) (has-passenger ?t ?p))
        :effect (and (not (has-passenger ?t ?p)) (at ?p ?l))
    )

    (:action drive
        :parameters (?t - taxi ?from - location ?to - location)
        :precondition (and (at ?t ?from) (move-space ?to) (not (bush-at ?b ?to)))
        :effect (and (not (at ?t ?from)) (at ?t ?to))
  )

)