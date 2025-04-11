% STEP 1: Feature Extraction

% Folder containing banana images
imageFolder = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab05-ColorClustering\'; % Update this path
imageFiles = dir(fullfile(imageFolder, '*.jpg')); % Get list of images
numImages = numel(imageFiles);

% Initialize an empty array to store feature vectors
feature_vector = [];

for i = 1:numImages
    % Read the input image
    img = imread(fullfile(imageFolder, imageFiles(i).name));
    img = imresize(img, [256, 256]); % Resize for consistency
    
    % Convert the image to HSV color space
    hsvImg = rgb2hsv(img);
    s = hsvImg(:, :, 2); % Saturation channel
    
    % STEP 1.1: Find a set of banana pixels in the image
    % Banana pixels: Saturation > 0.3 (threshold for detecting banana pixels)
    bananaMask = find(s >= 0.3); % Linear indices of banana pixels
    
    % Extract corresponding RGB values for the banana pixels
    imgR = img(:, :, 1); % Red channel
    imgG = img(:, :, 2); % Green channel
    imgB = img(:, :, 3); % Blue channel
    
    bananaR = imgR(bananaMask); % Red values of banana pixels
    bananaG = imgG(bananaMask); % Green values of banana pixels
    bananaB = imgB(bananaMask); % Blue values of banana pixels
    
    % STEP 1.2: Compute color features
    % Compute the mean of the color values for the banana pixels
    meanR = mean(bananaR);
    meanG = mean(bananaG);
    meanB = mean(bananaB);
    
    % Store the computed mean RGB values as a feature vector
    feature_vector = [feature_vector; [meanR, meanG, meanB]]; %#ok<AGROW>
end

% Display the extracted feature vectors
disp('Feature Vectors (RGB):');
disp(feature_vector);

% STEP 2: Banana Ripeness Clustering

% Perform hierarchical clustering
Z = linkage(feature_vector, 'complete', 'euclidean');

% Create clusters (number of clusters corresponds to ripeness stages)
numClusters = 4; % You can adjust this based on your ripeness categories
clusterLabels = cluster(Z, 'maxclust', numClusters);

% Display the cluster labels
disp('Cluster Labels:');
disp(clusterLabels);

% Visualize the clusters in a 3D feature space (RGB)
figure;
scatter3(feature_vector(:, 1), feature_vector(:, 2), feature_vector(:, 3), ...
    240, clusterLabels, 'fill');
xlabel('R (Red)');
ylabel('G (Green)');
zlabel('B (Blue)');
title('Banana Ripeness Clustering');
grid on;

% Save the results as a table
resultsTable = table((1:numImages)', clusterLabels, ...
    'VariableNames', {'ImageNumber', 'ClusterLabel'});
disp('Clustering Results:');
disp(resultsTable);
