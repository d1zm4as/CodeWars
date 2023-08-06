fn update_light(current: &str) -> &str {
    match current{
        "green"=>"yellow",
        "yellow"=>"red",
        "red"=>"green",
        _=>"dunno",
    }
}