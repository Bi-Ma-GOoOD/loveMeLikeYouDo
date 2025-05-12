im = imread("scrambled_image.tif");
imshow(im);
D = size(im);

copy = zeros(size(im));
copy = uint8(copy);

for i = 1:909
    for j = 1:1170
        copy(r(i), c(j),1) = im(i, j,1);
        copy(r(i), c(j),2) = im(i, j,2);
        copy(r(i), c(j),3) = im(i, j,3);
    end
end
imshow(copy);
