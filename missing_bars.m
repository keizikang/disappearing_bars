close all
clear
clc

%% missing bars 가설 구현

fig_w = 251;
bar_width = 0.1;
n_bars = 100;
mag = fig_w/n_bars;

bar_centers = linspace(1, fig_w, 100);
bar_lefts = bar_centers - bar_width/2*mag;
bar_rights = bar_centers + bar_width/2*mag;
bar_showing = (round(bar_rights) - round(bar_lefts))>0;

x = 1:n_bars;
y = x.*bar_showing;

figure, 
bar(x, y, EdgeColor="none");


%% width 0.1짜리 bar 100개

figure, 
bar(1:100, 1:100, .1, EdgeColor="none")


%% 기본 bar width로 bar 100개

figure, 
bar(1:100, 1:100, EdgeColor="none")


%% bar width를 [.1, .2, .3, .4]로 바꿔가며 테스트

figure, 
fig_w = 196;
bar_widths = [.1, .2, .3, .4];
for i = 1:length(bar_widths)
    bar_width = bar_widths(i);
    n_bars = 100;
    mag = fig_w/n_bars;
    
    bar_centers = linspace(1, fig_w, 100);
    bar_lefts = bar_centers - bar_width/2*mag;
    bar_rights = bar_centers + bar_width/2*mag;
    bar_showing = (round(bar_rights) - round(bar_lefts))>0;
    
    x = 1:n_bars;
    y = x.*bar_showing;

    subplot(1, 4, i)
    bar(x, y, bar_width, EdgeColor="none");
end

