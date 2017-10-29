function y = box_intersect(coord,sqr,array)
[~,num] = size(array);
% === boundaries of the box
rightx = coord(1) + sqr;
leftx = coord(1) - sqr;
topy = coord(2) + sqr;
boty = coord(2) - sqr;
% ===
smallest = inf;
smallest2 = inf;
smallesti = -1;
smallest2i = -1;
for i = 1:num
    % looping over every normal line. for each normal line, check
    % intersection with the four corners of the 'box'.
    N = array(4,i);
    % array(2,num) is x-coordinate
    % array(3,num) is y-coordinate
    y01 = N*(leftx-array(2,i)) + array(3,i); % intersection with left vertical
    y02 = N*(rightx-array(2,i)) + array(3,i); % intersection with right vertical
    x02 = (topy + N*array(2,i) - array(3,i))/N;
    x01 = (boty + N*array(2,i) - array(3,i))/N;
    a1 = ((y01 >= boty) && (y01 <= topy));
    a2 = ((y02 >= boty) && (y02 <= topy));
    a3 = ((x02 >= leftx) && (x02 <= rightx));
    a4 = ((x01 >= leftx) && (x01 <= rightx));
%     if i == 1
%         disp(array(2,i));
%         disp(array(3,i));
%         disp(topy);
%         disp(boty);
%         disp(N);
%         disp((topy + N*array(2,i) - array(3,i))/N);
%     disp(x02);
%     disp(x01);
%     disp(y02);
%     disp(y01);
%     end 
   if  a1 || a2 || a3 || a4 % exists an intersect
       disp('reached');
        dist = (coord(1) - array(2,i))^2 + (coord(2) - array(3,i))^2;
        if dist < smallest
            smallest2 = smallest;
            smallest2i = smallesti;
            smallest = dist;
            smallesti = i;
        elseif dist > smallest && dist <= smallest2
            smallest2 = dist;
            smallest2i = i;
        end
         disp(dist);
    end
end
if smallesti == -1
    if coord(1) < array(2,num)
        smallesti = 0;
        smallest2i = 0;
    else
        smallesti = num;
        smallest2i = num;
    end 
end 
if smallesti == smallest2i
    y = 0.01 + smallesti*(0.98/num);
else
    y = 0.01 + (smallesti + smallest2i)/2*(0.98/num);
end