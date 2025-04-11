%% 00-Preprocessing
image_ref = imread('reference_sm.jpg');
imageFolder = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab08-findingStarbucks\starbucks35_dataset\';
imageFiles = dir(fullfile(imageFolder, '*.jpg'));
numImage = numel(imageFiles);

image_ref_gray = rgb2gray(image_ref);

for i = 1:numImage
    img_get = imread(fullfile(imageFolder, imageFiles(i).name));
    img2_gray = rgb2gray(img_get);

%% 01-Feature Detection
% Harris corner detection
% points_Harris = detectHarrisFeatures(img2_gray);
% points_Harris_ref = detectHarrisFeatures(image_ref_gray);
% SURF feature detection
points_SURF = detectSURFFeatures(img2_gray);
points_SURF_ref = detectSURFFeatures(image_ref_gray);
% MSER feature detection
% points_MSER = detectMSERFeatures(img2_gray);
% points_MSER_ref = detectMSERFeatures(image_ref_gray);

%% 02-Feature Description
% Extract features using SURF
[features, validPoints] = extractFeatures(img2_gray, points_SURF);
[features_ref, validPoints_ref] = extractFeatures(image_ref_gray, points_SURF_ref);
%% 03-Feature Matching
indexPairs = matchFeatures(features_ref, features, 'Method', 'NearestNeighborRatio',...
                            'MatchThreshold', 2.5, 'MaxRatio', 0.85);
% store coordinated of matched pair feature
matchedPoints1 = validPoints_ref(indexPairs(:, 1));
matchedPoints2 = validPoints(indexPairs(:, 2));
%% 04-Display corresponding feature points
% falsecolor: Overlay the images by creating a composite red-cyan image showing I1 as red and I2 as cyan.
% blend: Overlay image_ref and image_input by using alpha blending.
% montage: Place image_ref and image_input next to each other in the same
% - image
if ~isempty(indexPairs)
    matchedPoints1 = validPoints_ref(indexPairs(:, 1));
    matchedPoints2 = validPoints(indexPairs(:, 2));

    % Display matches
    fprintf('matches found for image %d. \n', i);
    figure;
    showMatchedFeatures(image_ref, img_get, matchedPoints1, matchedPoints2, "montage");
else
    fprintf('No matches found for image %d.\n', i);
    figure;
    showMatchedFeatures(image_ref, img_get, matchedPoints1, matchedPoints2, "montage");
end
end