using DelimitedFiles

function weather()
    weather_data = readdlm("weather.dat")
    day_number = weather_data[2:end,1]
    day_number[end,1] = 31
    max_temp = weather_data[2:end,2]
    for i=1:size(max_temp,1)
        if occursin("*",string(max_temp[i]))
            max_temp[i] = rstrip(max_temp[i], '*')
            max_temp[i] = parse(Int,max_temp[i])
        end
    end
    min_temp = weather_data[2:end,3]
    for j=1:size(min_temp,1)
        if occursin("*",string(min_temp[j]))
            min_temp[j] = rstrip(min_temp[j], '*')
            min_temp[j] = parse(Int,min_temp[j])
        end
    end
    temp_spread = max_temp - min_temp
    table = hcat(day_number,temp_spread)
    return table
end

function football()
    football_data = readdlm("football.dat")
    temp = football_data[2:end,1]
    temp2 = football_data[2:end,2]
    football_data[2:end,1] = temp2
    football_data[2:end,2] = temp
    data = Dict("Team"=>football_data[2:end,1],"P"=>football_data[2:end,2],
                "G"=>football_data[2:end,3],"W"=>football_data[2:end,4],
                "L"=>football_data[2:end,5],"D"=>football_data[2:end,6],
                "F"=>football_data[2:end,7],"A"=>football_data[2:end,9],
                "Pts"=>football_data[2:end,10])
    go_for = data["F"]
    go_for = vec(go_for)
    go_ag = data["A"]
    go_ag = vec(go_ag)
    filter!(e->e!="",go_for)
    filter!(e->e!="",go_ag)
    goal_dif = map(abs, go_for - go_ag)
    min = minimum(goal_dif)
    ind = findall(x->x==min, goal_dif)
    filter!(e->e!="",data["Team"])
    ans = data["Team"][ind]
    return ans
end
