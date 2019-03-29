function mergesort(a)
    @assert size(a,2) == 1
    n = size(a,1)
    if n > 1
        return merge_function(mergesort(a[1:Int(floor(n/2))]),
                                    mergesort(a[(Int(floor(n/2))+1):n]))
    else
        return a
    end
end

function merge_function(x,y)
    @assert size(x,2) == 1
    @assert size(y,2) == 1
    k = size(x, 1)
    l = size(y, 1)
    if k == 0
        return y
    end
    if l == 0
        return x
    end
    if x[1] <= y[1]
        return vcat(x[1],merge_function(x[2:k],y[1:l]))
    else
        return vcat(y[1],merge_function(x[1:k],y[2:l]))
    end
end
