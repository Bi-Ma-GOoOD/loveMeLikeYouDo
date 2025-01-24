maskHand = imread('lymphomalplzhang03_shade.jpg');
maskBackground = ~maskHand;
imshow(maskBackground)
title('Background Mask')